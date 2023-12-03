# ./seeders/services.py

from app.models import Service
from app import db

def seed_services():
    """Seed the services table with data"""
    services_data = [
        {
            "name": "Template-based Website Solutions",
            "image_filename": "service-one.png",
            "details": {
                "description": "Cost-effective, template-based website solutions ideal for small businesses and startups looking for a quick and efficient online presence. Includes customization options to align with brand identity."
            },
            "price": 500.0,
            "currency": "USD",
            "is_available": True,
            "category": "Development",
            "duration": "project-based",
            "early_eligible": True,
            "experimental": False,
            "note": "Includes basic customization options. Additional features may incur extra costs.",
            "target_audiences": ["Startups", "Small Businesses", "Personal Brands", "Freelancers", "Non-profits"]
        },
        {
            "name": "Chemical Process Software Integration",
            "image_filename": "service-two.png",
            "details": {
                "description": "Specialized consulting for integrating chemical engineering principles with software applications, suitable for process simulation, data analysis, and automation in the chemical industry.",
            },
            "price": 200.0,
            "currency": "USD",
            "is_available": True,
            "category": "Consulting",
            "duration": "flat",
            "early_eligible": True,
            "experimental": False,
            "note": "This service is only available for chemical engineering projects. Pricing for post consultation services will be determined on a case-by-case basis if applicable.",
            "target_audiences": ["Petrochemical Refining", "Plastics Manufacturing", "Pharmaceuticals", "Food and Beverage Industry", "Environmental and Waste Management", "Research and Development", "Academic Institutions", "Energy Sector", "Manufacturing Industry", "Chemical Regulatory Agencies"]
        },
        {
            "name": "Sales Software Integration Consulting",
            "image_filename": "service-three.png",
            "details": {
                "description": "Consulting services to enhance sales strategies through software solutions, including CRM integration, sales data analysis, and digital marketing tools."
            },
            "price": 80.0,
            "currency": "USD",
            "is_available": False,
            "category": "Consulting",
            "duration": "flat",
            "early_eligible": True,
            "experimental": False,
            "note": "This service is only available for sales projects. Pricing for post consultation services will be determined on a case-by-case basis if applicable.",
            "target_audiences": ["Small Businesses", "Startups", "Entrepreneurs", "Sales Professionals", "Marketing Professionals", "Business Development Professionals", "Sales Managers", "Sales Directors", "Sales Executives", "Sales Representatives", "Sales Consultants", "Sales Engineers", "Sales Coaches", "Sales Trainers", "Sales Recruiters", "Sales Analysts", "Sales Operations Managers", "Sales Operations Analysts", "Sales Operations Specialists", "Sales Operations Coordinators", "Sales Operations Administrators", "Sales Operations Directors", "Sales Operations Executives", "Sales Operations Consultants", "Sales Operations Engineers", "Sales Operations Trainers", "Sales Operations Recruiters", "Sales Operations Coaches", "Sales Operations Analysts", "Sales Operations Specialists", "Sales Operations Coordinators", "Sales Operations Administrators", "Sales Operations Directors", "Sales Operations Executives", "Sales Operations Consultants", "Sales Operations Engineers", "Sales Operations Trainers", "Sales Operations Recruiters", "Sales Operations Coaches"]
        },
        {
            "name": "AI Productivity Enhancement Seminar",
            "image_filename": "service-four.png",
            "details": {
                "description": "A comprehensive seminar for teams or organizations on leveraging AI technologies to boost productivity, covering practical applications, case studies, and the latest trends."
            },
            "price": 300.0,
            "currency": "USD",
            "is_available": True,
            "category": "Event",
            "duration": "flat",
            "early_eligible": True,
            "experimental": True,
            "note": "Event subject to availability. Please contact me for more information and a more detailed cost estimate as this service is experimental.",
            "target_audiences": ["Everyone"]
        },
        {
            "name": "One-on-One Software Tutoring",
            "image_filename": "service-five.png",
            "details": {
                "description": "Personalized tutoring sessions in software development, tailored to individual learning goals and skill levels."
            },
            "price": 30.0,
            "currency": "USD",
            "is_available": True,
            "category": "Education",
            "duration": "hourly",
            "early_eligible": False,
            "experimental": False,
            "note": "Subject to availability. Please contact me for more information on scheduling.",
            "target_audiences": ["Students", "Professionals", "Entrepreneurs", "Small Businesses", "Startups"]
        },
        {
            "name": "Standalone Software Development Services",
            "image_filename": "service-six.png",
            "details": {
                "description": "Custom software development services, including web applications, automation tools, and bespoke software solutions."
            },
            "price": 250.0,
            "currency": "USD",
            "is_available": True,
            "category": "Development",
            "duration": "flat",
            "early_eligible": True,
            "experimental": True,
            "note": "Subject to availability. Please contact me for more information and a more detailed cost estimate as this service is experimental.",
            "target_audiences": ["Small Businesses", "Startups", "Entrepreneurs"]
        },
        {
            "name": "Long-Term Project Engagement",
            "image_filename": "service-seven.png",
            "details": {
                "description": "Dedicated support for long-term projects (3+ months), offering in-depth involvement in project planning, execution, and management across various domains."
            },
            "price": 5000.0,
            "currency": "USD",
            "is_available": True,
            "category": "Development",
            "duration": "monthly",
            "early_eligible": True,
            "experimental": True,
            "note": "Subject to availability. Please contact me for more information and a more detailed cost estimate as this service is experimental.",
            "target_audiences": ["Small Businesses", "Startups", "Entrepreneurs", "Mid-Sized Businesses", "Large Businesses", "Enterprise Businesses", "Corporations", "Government Agencies", "Non-Profit Organizations", "Academic Institutions", "Research Institutions", "Research and Development", "Energy Sector", "Manufacturing Industry", "Chemical Regulatory Agencies"]
        },
        {
            "name": "Customized Workshop on Adaptive AI Technologies",
            "image_filename": "service-eight.png",
            "details": {
                "description": "Tailored workshops for organizations interested in exploring adaptive AI technologies, with hands-on sessions and interactive learning experiences."
            },
            "price": 400.0,
            "currency": "USD",
            "is_available": True,
            "category": "Event",
            "duration": "flat",
            "early_eligible": True,
            "experimental": True,
            "note": "Event subject to availability. Please contact me for more information and a more detailed cost estimate as this service is experimental.",
            "target_audiences": ["Everyone"]
        },
        {
            "name": "Custom Website/Webapp Development",
            "image_filename": "service-nine.png",
            "details": {
                "description": "Bespoke web application development services, offering tailor-made solutions for unique business needs, including e-commerce sites, interactive web applications, and enterprise solutions."
            },
            "price": 5000.0,
            "currency": "USD",
            "is_available": True,
            "category": "Development",
            "duration": "project-based",
            "early_eligible": True,
            "experimental": True,
            "note": "Contact for a customized quote based on specific project requirements.",
            "target_audiences": ["Startups", "Small to Medium Businesses", "Large Corporations", "E-commerce Ventures", "Educational Institutions"]
        },
        {
            "name": "Sales Strategy Development and Optimization",
            "image_filename": "service-ten.png",
            "details": {
                "description": "Developing and optimizing sales strategies using data-driven insights, focusing on maximizing efficiency and effectiveness in sales processes."
            },
            "price": 50.0,
            "currency": "USD",
            "is_available": True,
            "category": "Consulting",
            "duration": "recurrent",
            "early_eligible": True,
            "experimental": True,
            "note": "Subject to availability. Please contact me for more information and a more detailed cost estimate as this service is experimental.",
            "target_audiences": ["Small Businesses", "Startups", "Entrepreneurs", "Sales Professionals", "Marketing Professionals", "Business Development Professionals", "Sales Managers", "Sales Directors", "Sales Executives", "Sales Representatives", "Sales Consultants", "Sales Engineers", "Sales Coaches", "Sales Trainers", "Sales Recruiters", "Sales Analysts", "Sales Operations Managers", "Sales Operations Analysts", "Sales Operations Specialists", "Sales Operations Coordinators", "Sales Operations Administrators", "Sales Operations Directors", "Sales Operations Executives", "Sales Operations Consultants", "Sales Operations Engineers", "Sales Operations Trainers", "Sales Operations Recruiters", "Sales Operations Coaches", "Sales Operations Analysts", "Sales Operations Specialists", "Sales Operations Coordinators", "Sales Operations Administrators", "Sales Operations Directors", "Sales Operations Executives", "Sales Operations Consultants", "Sales Operations Engineers", "Sales Operations Trainers", "Sales Operations Recruiters", "Sales Operations Coaches"]
        }
    ]

    for service_data in services_data:
        existing_service = Service.query.filter_by(name=service_data['name']).first()
        if not existing_service:
            service = Service(**service_data)
            db.session.add(service)

    db.session.commit()
