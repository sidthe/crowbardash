from django.utils.translation import ugettext_lazy as _
from horizon import tables


class HardwareTable(tables.DataTable):
    hostname = tables.Column("hostname", verbose_name=_("Hostname"))
    cpu = tables.Column("cpu", verbose_name=_("CPU"))
    ram = tables.Column("ram", verbose_name=_("RAM"))
    mac_address = tables.Column("mac_address", verbose_name=_("MAC Address"))
    platform = tables.Column("platform", verbose_name=_("Platform"))

    class Meta:
        name = "hardware_table"
        verbose_name = _('Hardware Table')
