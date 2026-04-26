"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .abb import AbbFetcher
from .airtac import AirtacFetcher
from .amada import AmadaFetcher
from .caterpillar import CaterpillarFetcher
from .delta import DeltaFetcher
from .dmg_mori import DmgMoriFetcher
from .fanuc import FanucFetcher
from .goodway import GoodwayFetcher
from .hiwin import HiwinFetcher
from .itw import ItwFetcher
from .jtekt import JtektFetcher
from .keyence import KeyenceFetcher
from .lincoln_electric import LincolnElectricFetcher
from .makino import MakinoFetcher
from .mitsubishi_electric import MitsubishiElectricFetcher
from .okuma import OkumaFetcher
from .parker_hannifin import ParkerHannifinFetcher
from .rockwell import RockwellFetcher
from .schneider import SchneiderFetcher
from .siemens import SiemensFetcher
from .thk import ThkFetcher
from .tongtai import TongtaiFetcher

FETCHERS = {
    "abb": AbbFetcher,
    "airtac": AirtacFetcher,
    "amada": AmadaFetcher,
    "caterpillar": CaterpillarFetcher,
    "delta": DeltaFetcher,
    "dmg_mori": DmgMoriFetcher,
    "fanuc": FanucFetcher,
    "goodway": GoodwayFetcher,
    "hiwin": HiwinFetcher,
    "itw": ItwFetcher,
    "jtekt": JtektFetcher,
    "keyence": KeyenceFetcher,
    "lincoln_electric": LincolnElectricFetcher,
    "makino": MakinoFetcher,
    "mitsubishi_electric": MitsubishiElectricFetcher,
    "okuma": OkumaFetcher,
    "parker_hannifin": ParkerHannifinFetcher,
    "rockwell": RockwellFetcher,
    "schneider": SchneiderFetcher,
    "siemens": SiemensFetcher,
    "thk": ThkFetcher,
    "tongtai": TongtaiFetcher,
}
