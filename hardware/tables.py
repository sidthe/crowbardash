from django.utils.translation import ugettext_lazy as _
from horizon import tables


class HardwareTable(tables.DataTable):
    hostname = Column('hostname', verbose_name=_('Hostname'))
    cpu = Column('cpu', verbose_name=_('CPU'))
    ram = Column('ram', verbose_name=_('RAM'))
    mac_address = Column('mac_address', verbose_name=_('MAC Address'))
    platform = Column('platform', verbose_name=_('Platform'))

    class Meta:
        name = 'hardware_table'
        verbose_name = _('Hardware Table')
        multi_select = False
