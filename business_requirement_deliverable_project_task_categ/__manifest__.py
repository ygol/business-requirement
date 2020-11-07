# © 2016-2019 Elico Corp (https://www.elico-corp.com).
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    "name": "Business Requirement Deliverable Project Task Categ",
    'category': 'Business Requirements Management',
    'summary': 'Adds Task Categories to your Business Requirement Resources',
    "version": "13.0.2.0.0",
    "website": "https://github.com/OCA/business-requirement",
    "author": "Elico Corp,Yves Goldberg (Ygol Internetwork), Odoo Community Association (OCA)",
    "license": "LGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "hr_timesheet",
        "business_requirement_deliverable_project",
        "project_category",
        "business_requirement_deliverable_resource",
    ],
    'image': [
        'static/description/icon.png',
        'static/img/bus_req_category.png'
    ],
    "data": [
        # "views/business_requirement_deliverable.xml",
    ],
    'demo': [
        'data/business_requirement_deliverable_project_task_categ_demo.xml'
    ],

}

o
