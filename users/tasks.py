from applications.models import (Application)
from faqs.models import (Faq)
from houses.models import (House)
from medias.models import (Media)
from organisations.models import (Organisation)
from rebates.models import (Rebate)
from reports.models import (Report)
#from tickets.models import ()
from users.models import (CustomUser)


def initialise_app_for(user):

    return json_data