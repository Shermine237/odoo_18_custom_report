{
    'name': 'Rapport de Facture Personnalisé (Studio)',
    'version': '1.0',
    'summary': 'Remplace le rapport de facture Odoo par un design personnalisé via import Studio.',
    'description': """
Ce module, importable via Odoo Studio, remplace le rapport de facture standard par un design personnalisé.
    """,
    'category': 'Accounting/Localizations',
    'author': 'Charlie Rostant YOSSA',
    'website': '',
    'depends': ['account', 'web_studio'],
    'data': [
        'views/invoice_header.xml',
        'views/invoice_footer.xml',
        'views/invoice_body.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
