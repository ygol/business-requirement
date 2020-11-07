# Copyright 2020 Yves Goldberg (Ygol InternetWork)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Business Requirement Deliverable Role',
    "category": "Business Requirements Management",
    'description': """
        Add the notion of stakeholer role to deliverable lines""",
    'version': '13.0.2.0.0',
    'license': 'AGPL-3',
    'author': 'Yves Goldberg (Ygol InternetWork)',
    'website': 'http://www.ygol.com',
    'depends': [
        'business_requirement_deliverable'
    ],
    'data': [
        'views/business_requirement_deliverable.xml',
        'security/stakeholder_role.xml',
        'views/stakeholder_role.xml',
    ],
    'demo': [
        'demo/stakeholder_role.xml',
    ],
}
