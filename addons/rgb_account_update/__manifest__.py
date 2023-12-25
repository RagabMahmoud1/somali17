{
    'name': "RGB Account Update",
    'summary': """
        summary
    """,
    'description': """
        description
    """,
    'author': "Ragab",
    'contributors': [
        'Ragab Deaf <ragabdeaf93@outlook.com>',
    ],
    'version': '1.0',
    'depends': ['base', 'account', 'om_account_accountant'],
    'data': [
        'security/groups.xml',
        'report/rgb_format.xml',
        'security/ir.model.access.csv',
        'views/account_report.xml',
        'views/report_invoice.xml',
    ],
    'license': 'OPL-1',
    "pre_init_hook": None,
    "post_init_hook": None,
}
# -*- coding: utf-8 -*-
