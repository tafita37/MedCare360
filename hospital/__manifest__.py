{
    'name': 'Hospital',
    'version': '1.0',
    'depends': ['sale'],
    'data': [
        'data/master_data/res_groups_data.xml',  
        'data/master_data/res_users_data.xml',  
        'data/demo_data/hospital_severity_level_data.xml',  
        'data/demo_data/hospital_efficiency_level_data.xml',  
        'data/demo_data/hospital_symptom_data.xml',  

        'security/ir.model.access.csv',  

        'views/hospital_disease_views.xml',
        'views/hospital_disease_type_views.xml',
        'views/hospital_symptom_views.xml',
        'views/product_template_views.xml',
        'views/hospital_menu_views.xml'
    ],
    'author': 'Moi',
    'category': 'Uncategorized',
    'description': 'Hospital is the core module managing the overall structure of the hospital, including patient data, staff, and essential hospital operations.',
    'installable': True,
    'application': True,
}
