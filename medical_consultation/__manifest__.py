{
    'name': 'medical_consultation',
    'version': '1.0',
    'depends': ['hospital'],
    'data': [
        'security/medical_consultation_security.xml',
        'security/ir.model.access.csv',
          
        'views/medical_consultation_request_views.xml',
        'views/medical_consultation_nurse_views.xml',
        'views/medical_consultation_menu_views.xml',

        'wizard/medical_consultation_affectation_nurse_wizard_views.xml',
        'wizard/medical_consultation_affectation_doctor_wizard_views.xml',
    ],
    'author': 'Moi',
    'category': 'Uncategorized',
    'description': 'The Medical Consultation module extends the hospital management system by providing a comprehensive and user-friendly platform for managing patient consultations. It enables patients to schedule appointments, receive detailed medical diagnoses, and access follow-up care instructions. Integrated with the core hospital module, it streamlines the consultation process for healthcare professionals, ensuring accurate record-keeping and efficient service delivery.',
    'installable': True,
    'application': True,
}
