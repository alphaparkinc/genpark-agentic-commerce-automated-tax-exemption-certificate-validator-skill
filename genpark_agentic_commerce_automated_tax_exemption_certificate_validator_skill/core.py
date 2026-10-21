# -*- coding: utf-8 -*-
"""B2B Sales Tax Exemption Certificate Validator for GenPark Agentic Commerce."""
import json
from typing import Dict, Any

class SalesTaxExemptionCertificateValidator:
    @staticmethod
    def validate_resale_certificate(state_code: str, tax_id_number: str, business_name: str, certificate_expiration_date: str = "2027-12-31") -> Dict[str, Any]:
        is_valid_format = len(tax_id_number.replace("-", "")) in [8, 9, 10, 11]
        return {"state": state_code.upper(), "tax_id": tax_id_number, "business": business_name, "is_valid": is_valid_format, "audit_status": "EXEMPTION_GRANTED" if is_valid_format else "INVALID_TAX_ID"}

    @staticmethod
    def calculate_tax_waived_order_total(subtotal_usd: float, standard_state_tax_rate_pct: float) -> Dict[str, Any]:
        tax_saved = round(subtotal_usd * (standard_state_tax_rate_pct / 100.0), 2)
        return {"order_subtotal_usd": subtotal_usd, "tax_rate_exempted_pct": standard_state_tax_rate_pct, "sales_tax_waived_usd": tax_saved, "final_invoice_amount_usd": subtotal_usd}
