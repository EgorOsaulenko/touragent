from flask import Blueprint, render_template, request, redirect, flash
from travel_agency.db import Session
from travel_agency.db.models.tour import Tour
from travel_agency.data.admin_password import ADMIN_PASSWORD

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
            return redirect("/")
        else:
            flash("Невірний пароль адміністратора!")

    return render_template("add_tour.html")
