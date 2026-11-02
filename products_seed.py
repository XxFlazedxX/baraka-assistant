# products_seed.py
"""
Baraka Al-Sanabel (basc-sa.com) real product catalog.
Source: public product page + company profile.
14 pasta shapes across 2 lines (Classic + Whole Wheat), 4 brands.
"""

BRANDS = [
    {"name": "Baraka Al-Sanabel", "name_ar": "بركة السنابل",
     "positioning": "Flagship brand, Swiss durum wheat, everyday premium pasta."},
    {"name": "Rovito", "name_ar": "روفيتو",
     "positioning": "Italian-style premium line for HoReCa and export."},
    {"name": "Sanbalat", "name_ar": "سنبلات",
     "positioning": "Value family pack line for local retail."},
    {"name": "Nooli", "name_ar": "نولي",
     "positioning": "Modern youth-oriented line, smaller packs."},
]

CERTIFICATIONS = ["ISO 22000:2018", "SFDA (Saudi Food & Drug Authority)"]

EXPORT_MARKETS = [
    "GCC (Saudi Arabia, UAE, Kuwait, Qatar, Bahrain, Oman)",
    "North Africa (Egypt, Morocco, Algeria, Tunisia, Libya)",
    "Europe (UK, France, Germany, Netherlands)",
    "North America (USA, Canada)",
    "Southeast Asia (Indonesia, Malaysia)",
    "East Africa (Sudan, Ethiopia, Somalia)",
]

MANUFACTURING = {
    "wheat": "Swiss durum wheat",
    "technology": "Swiss milling and extrusion lines",
    "factory_location": "Jeddah, Saudi Arabia",
    "quality": "ISO 22000:2018 certified, SFDA approved",
}

PRODUCTS = [
    # Classic line
    {"name": "Spaghetti", "name_ar": "سباجيتي", "line": "classic", "shape": "long, round", "whole_wheat": False},
    {"name": "Spaghettini", "name_ar": "سباجيتيني", "line": "classic", "shape": "long, thin round", "whole_wheat": False},
    {"name": "Vermicelli", "name_ar": "شعرية", "line": "classic", "shape": "long, very thin", "whole_wheat": False},
    {"name": "Fettuccine", "name_ar": "فيتوتشيني", "line": "classic", "shape": "long, flat ribbon", "whole_wheat": False},
    {"name": "Penne Rigate", "name_ar": "بيني ريجاتي", "line": "classic", "shape": "short, ridged tube, angled cut", "whole_wheat": False},
    {"name": "Pipe Rigati", "name_ar": "بايب ريجاتي", "line": "classic", "shape": "short, ridged curved tube", "whole_wheat": False},
    {"name": "Fusilli", "name_ar": "فوزيلي", "line": "classic", "shape": "short, spiral", "whole_wheat": False},
    {"name": "Conchiglie", "name_ar": "كونكيلي", "line": "classic", "shape": "short, shell", "whole_wheat": False},
    {"name": "Ditalini Lisci", "name_ar": "ديتاليني ليسي", "line": "classic", "shape": "short, smooth mini tube", "whole_wheat": False},
    {"name": "Ditalini Rigati", "name_ar": "ديتاليني ريجاتي", "line": "classic", "shape": "short, ridged mini tube", "whole_wheat": False},
    {"name": "Sedani", "name_ar": "سيداني", "line": "classic", "shape": "short, ridged tube, straight cut", "whole_wheat": False},
    {"name": "Chiffari Rigati", "name_ar": "شيفاري ريجاتي", "line": "classic", "shape": "short, ridged curved tube", "whole_wheat": False},
    {"name": "Orzo", "name_ar": "أورزو", "line": "classic", "shape": "short, rice-shaped", "whole_wheat": False},
    # Whole wheat line
    {"name": "Spaghetti (Whole Wheat)", "name_ar": "سباجيتي (قمح كامل)", "line": "whole_wheat", "shape": "long, round", "whole_wheat": True},
    {"name": "Penne Rigate (Whole Wheat)", "name_ar": "بيني ريجاتي (قمح كامل)", "line": "whole_wheat", "shape": "short, ridged tube", "whole_wheat": True},
    {"name": "Ditalini Rigati (Whole Wheat)", "name_ar": "ديتاليني ريجاتي (قمح كامل)", "line": "whole_wheat", "shape": "short, ridged mini tube", "whole_wheat": True},
    {"name": "Sedani (Whole Wheat)", "name_ar": "سيداني (قمح كامل)", "line": "whole_wheat", "shape": "short, ridged tube", "whole_wheat": True},
]