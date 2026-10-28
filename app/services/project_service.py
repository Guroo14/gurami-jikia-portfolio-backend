PROJECTS = [
    {
        "id": "ml-project",
        "title": "ML Project",
        "description": "A practical machine-learning project focused on data analysis, preprocessing, feature engineering and model development.",
        "category": "AI / ML",
        "technologies": ["Python", "Pandas", "NumPy", "Scikit-learn", "Matplotlib"],
        "github_url": None,
        "live_demo_url": None,
        "image": "ml",
        "featured": True,
        "status": "Personal project",
    },
    {
        "id": "pycasino",
        "title": "PyCasino",
        "description": "A Python desktop application demonstrating GUI development, database integration and application logic through login, registration, Blackjack and Baccarat.",
        "category": "Python",
        "technologies": ["Python", "PyQt5", "SQLite"],
        "github_url": None,
        "live_demo_url": None,
        "image": "pycasino",
        "featured": True,
        "status": "Personal project",
    },
    {
        "id": "shopsite",
        "title": "ShopSite",
        "description": "A web-development project included as part of my hands-on software development work.",
        "category": "Web",
        "technologies": [],
        "github_url": None,
        "live_demo_url": None,
        "image": "shopsite",
        "featured": False,
        "status": "Personal project",
    },
]


def get_projects() -> list[dict]:
    return PROJECTS
