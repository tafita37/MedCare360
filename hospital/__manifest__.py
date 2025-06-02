{
    'name': 'Hospital',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'data/master_data/res_groups_data.xml',  
        'data/demo_data/res_users_data.xml',  
        'data/demo_data/hospital_severity_level.xml',  
        'security/ir.model.access.csv',  
        'views/hospital_disease_views.xml',
        'views/hospital_disease_type_views.xml',
        'views/hospital_symptom_views.xml',
        'views/hospital_menu_views.xml'
    ],
    'author': 'Moi',
    'category': 'Uncategorized',
    'description': 'Hospital is the core module managing the overall structure of the hospital, including patient data, staff, and essential hospital operations.',
    'installable': True,
    'application': True,
}
