"""Stayntouch PMS reservation column mappings for REVREBEL standardization."""

from __future__ import annotations

from typing import Dict


STAYNTOUCH_COLUMN_MAP: Dict[str, str] = {
    # Stayntouch display headers after normalize_header().
    "hotel_code": "property_code",
    "confirmation_number": "source_id",
    "created_at": "book_datetime",
    "arrival_date": "arrival_date",
    "departure_date": "departure_date",
    "cancel_date": "cx_date",
    "arrival_time": "arrival_time",
    "departure_time": "departure_time",
    "status": "rsvn_status",
    "adults": "adult_qty",
    "children": "child_qty",
    "infants": "infant_qty",
    "travel_agent_account_name": "travel_agent_name",
    "travel_agent_ar_number": "travel_agent_ar_number",
    "travel_agent_iata_number": "travel_agent_iata",
    "company_name": "company_name_map",
    "company_ar_number": "company_ar_number",
    "rate_code": "rate_code_map",
    "rate_type": "ratetype_map",
    "room_number": "room_number",
    "room_type": "roomtype_code_map",
    "payment_method_payment_type_value": "payment_method_map",
    "market_segment_name": "segment_map",
    "source_code": "source_code_map",
    "group_name": "group_name",
    "membership_class": "membership_class",
    "membership_type": "membership_type",
    "membership_number": "membership_number",
    "total_stay_amount": "total_rev",
    "rate_amount": "rate_amount",
    "guest_last_name": "guest_last_name",
    "guest_first_name": "guest_first_name",
    "guest_birthday": "guest_birth_date",
    "guest_email": "guest_email",

    # Stayntouch API/export headers after normalize_header().
    "create_date": "book_datetime",
    "created_date": "book_datetime",
    "arrival_date_original": "arrival_date_original",
    "departure_date_original": "departure_date_original",
    "travel_agent": "travel_agent_name",
    "travel_agent_ar": "travel_agent_ar_number",
    "company": "company_name_map",
    "company_ar": "company_ar_number",
    "rate": "rate_code_map",
    "payment_type": "payment_method_map",
    "market_segment": "segment_map",
    "source": "source_code_map",
    "group": "group_name",
    "total_amount": "total_rev",
    "rate_amount_for_total_stay": "rate_total_amount",
    "origin_of_booking": "channel_code_group_map",
    "segment": "segment_map",
    "travel_ar": "travel_agent_ar_number",
    "first_name": "guest_first_name",
    "last_name": "guest_last_name",
    "language_code": "language_code",
    "vip": "vip_code",
}


STAYNTOUCH_REPORT_ALIASES = {
    "stayntouch",
    "stayntouch_reservations",
    "stayntouch_reservation",
    "stayntouch_reservations_report",
    "stayntouch_last_month_reservations",
    "stayntouch_upcoming_reservations",
    # Common misspelling retained for compatibility.
    "stayintouch",
    "stayintouch_reservations",
}
