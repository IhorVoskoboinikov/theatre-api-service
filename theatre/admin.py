from django.contrib import admin

from .models import (
    TheatreHall,
    Genre,
    Actor,
    Play,
    Performance,
    Reservation,
    Ticket,
)


@admin.register(TheatreHall)
class TheatreHallAdmin(admin.ModelAdmin):
    fields = ("name",)
    search_help_text = "Search by play"
    list_per_page = 20


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    fields = ("name", "rows", "seats_in_row",)
    search_fields = ("name",)
    search_help_text = "Search by name"
    list_per_page = 20


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    fields = ("first_name", "last_name",)
    search_fields = ("first_name", "last_name")
    search_help_text = "Search by first name or last name"
    list_per_page = 20


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    fields = ("title", "genres", "actors")
    search_fields = ("title",)
    search_help_text = "Search by title"
    list_per_page = 20


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    fields = ("play", "theatre_hall", "show_time",)
    search_fields = ("play",)
    search_help_text = "Search by play"
    list_per_page = 20


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    fields = ("user", "created_at",)
    search_fields = ("user",)
    search_help_text = "Search by user"
    list_per_page = 20


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    fields = ("performance", "reservation", "row", "seat")
    search_fields = ("performance",)
    search_help_text = "Search by performance"
    list_per_page = 20
