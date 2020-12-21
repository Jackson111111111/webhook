import cfg
# <no> <report>
cfg.StrOpt('protocol',
           default='https',
           help='Default protocol to use when connecting to glance.')
# <yes> <report> PYTHON_HTTP_USAGE fk7d9r
cfg.StrOpt('protocol',
           default='http',
           help='Default protocol to use when connecting to glance.')