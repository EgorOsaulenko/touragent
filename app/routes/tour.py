from flask import Blueprint, render_template, request, redirect, flash, url_for
from app.db import Session
from app.db.models.tour import Tour
from app.db.models.booking import Booking
from app.data.admin_password import ADMIN_PASSWORD

tour_route = Blueprint("tours", __name__, url_prefix="/tours")

@tour_route.route("/add", methods=["GET", "POST"])
def add_tour():
    if request.method == "POST":
        name = request.form.get("name")
        destination = request.form.get("destination")
        price = request.form.get("price")
        duration_days = request.form.get("duration_days")
        description = request.form.get("description")
        password = request.form.get("password")

        if password == ADMIN_PASSWORD:
            with Session() as session:
                tour = Tour(
                    name=name,
                    destination=destination,
                    price=price,
                    duration_days=duration_days,
                    description=description
                )
                session.add(tour)
                session.commit()
            flash("Тур успішно додано!")
            return redirect(url_for("main.index"))
        else:
            flash("Невірний пароль адміністратора!")

    return render_template("add_tour.html")


@tour_route.route("/<int:tour_id>", methods=["GET", "POST"])
def tour_detail(tour_id):
    with Session() as session:
        tour = session.query(Tour).get(tour_id)
        if request.method == "POST":
            customer_name = request.form.get("customer_name")
            customer_email = request.form.get("customer_email")
            seats = request.form.get("seats")

            booking = Booking(
                tour_id=tour_id,
                customer_name=customer_name,
                customer_email=customer_email,
                seats=int(seats)
            )
            session.add(booking)
            session.commit()
            flash("Бронювання успішно здійснено!")
            return redirect(url_for("tours.list_tours"))

    return render_template("tour_detail.html", tour=tour)


