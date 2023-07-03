#!/usr/bin/env python


# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones intact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# manage.py dumpscript living_things.LivingThings
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script
import os, sys
from django.db import transaction

class BasicImportHelper:

    def pre_import(self):
        pass

    @transaction.atomic
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    # From Python 3.3 we can check e.name - string match is for backward compatibility.
    if 'import_helper' in str(e):
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
    from dateutil.tz import tzoffset
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports
    from general.models import GenreForURL
    from general.models import Article
    from general.models import Language

    # Processing model: living_things.models.LivingThings

    from living_things.models import LivingThings

    living_things_livingthings_1 = LivingThings()
    living_things_livingthings_1.name = 'African Elephant'
    living_things_livingthings_1.slug = 'african-elephant'
    living_things_livingthings_1.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_livingthings_1.habitat = None
    living_things_livingthings_1.species = None
    living_things_livingthings_1.article =  importer.locate_object(Article, "id", Article, "id", 172, {'id': 172, 'excerpt': 'African elephant', 'kicker': 'African elephant', 'content': '<p>The African elephant is a genus comprising two living elephant species the African bush elepha and the smaller African forest elephant (L. cyclotis). Both are social herbivores with grey skin iffer in the size and colour of their tusks and in the shape and size of their ears and skulls Both species are considered at heavy risk of extinction on the IUCN Red List; as of 2021 the bush elephant is considered endangered and the forest elephant is considered critically endangered. They are threatened</p>\r\n\r\n<p>From Wikipedia</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:35:07+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:35:21.428702+00:00")} ) 
    living_things_livingthings_1.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 7, {'id': 7, 'name': 'living-things/each'} ) 
    living_things_livingthings_1 = importer.save_or_locate(living_things_livingthings_1)

    living_things_livingthings_2 = LivingThings()
    living_things_livingthings_2.name = 'アフリカゾウ'
    living_things_livingthings_2.slug = 'african-elephant-jp'
    living_things_livingthings_2.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_livingthings_2.habitat = None
    living_things_livingthings_2.species = None
    living_things_livingthings_2.article =  importer.locate_object(Article, "id", Article, "id", 173, {'id': 173, 'excerpt': 'アフリカゾウ', 'kicker': 'アフリカゾウ', 'content': '<p>アフリカゾウは、アフリカブッシュゾウとアフリカフォレストゾウ（L. cyclotis）の2種からなる現生ゾウ属である。両種とも社会性草食動物で、牙の大きさや色、耳や頭蓋骨の形や大きさが異なるが、IUCNレッドリストでは絶滅の危険性が高いとされており、2021年現在、ブッシュゾウは絶滅危惧種、シンリンゾウは準絶滅危惧種とされている。絶滅の危機に瀕している</p>\r\n\r\n<p>Wikipediaより</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:35:56+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:36:06.851820+00:00")} ) 
    living_things_livingthings_2.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 7, {'id': 7, 'name': 'living-things/each'} ) 
    living_things_livingthings_2 = importer.save_or_locate(living_things_livingthings_2)

    living_things_livingthings_3 = LivingThings()
    living_things_livingthings_3.name = 'Blue And Yellow Macaw'
    living_things_livingthings_3.slug = 'blue-and-yellow-macaw'
    living_things_livingthings_3.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_livingthings_3.habitat = None
    living_things_livingthings_3.species = None
    living_things_livingthings_3.article =  importer.locate_object(Article, "id", Article, "id", 174, {'id': 174, 'excerpt': 'blue-and-yellow macaw', 'kicker': 'blue-and-yellow macaw', 'content': '<p>The blue-and-yellow macaw (Ara ararauna), also known as the blue-and-gold macaw, is a large South American parrot with mostly blue top parts and light orange underparts, with gradient hues of green on top of its head. It is a member of the large group of neotropical parrots known as macaws. It inhabits forest (especially varzea, but also in open sections of terra firme or unflooded forest), woodland and savannah of tropical South America. They are popular in aviculture because of their striking color, ability to talk, ready availability in the marketplace, and close bonding to humans. They can also live for 65-70 years.</p>\r\n\r\n<p>## Taxonomy The blue-and-yellow macaw was formally described by the Swedish naturalist Carl Linnaeus in 1758 in the tenth edition of his Systema Naturae. He placed it with all the other parrots in the genus Psittacus and coined the binomial name Psittacus ararauna. This macaw is now one of the eight extant species placed in the genus Ara that was erected in 1799 by the French naturalist Bernard Germain de Lac&eacute;p&egrave;de. The genus name is from ar&aacute; meaning &quot;macaw&quot; in the Tupi language of Brazil. The word is an onomatopoeia based on the sound of their call. The specific epithet ararauna comes from the Tupi Ar&aacute;ra &uacute;na meaning &quot;big dark parrot&quot; for the hyacinth macaw. The word ararauna had been used by the German naturalist Georg Marcgrave in 1648 in his Historia Naturalis Brasiliae.The species is monotypic: no subspecies are recognised.</p>\r\n\r\n<p>From Wikipedia</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:37:53+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:38:06.054236+00:00")} ) 
    living_things_livingthings_3.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 7, {'id': 7, 'name': 'living-things/each'} ) 
    living_things_livingthings_3 = importer.save_or_locate(living_things_livingthings_3)

    living_things_livingthings_4 = LivingThings()
    living_things_livingthings_4.name = 'ルリコンゴウインコ'
    living_things_livingthings_4.slug = 'blue-and-yellow-macaw-jp'
    living_things_livingthings_4.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_livingthings_4.habitat = None
    living_things_livingthings_4.species = None
    living_things_livingthings_4.article =  importer.locate_object(Article, "id", Article, "id", 175, {'id': 175, 'excerpt': 'blue-and-yellow macaw', 'kicker': 'blue-and-yellow macaw', 'content': '<p>blue-and-yellow macaw</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:39:17+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:39:28.981609+00:00")} ) 
    living_things_livingthings_4.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 7, {'id': 7, 'name': 'living-things/each'} ) 
    living_things_livingthings_4 = importer.save_or_locate(living_things_livingthings_4)

    living_things_livingthings_5 = LivingThings()
    living_things_livingthings_5.name = 'Oryx'
    living_things_livingthings_5.slug = 'oryx'
    living_things_livingthings_5.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_livingthings_5.habitat = None
    living_things_livingthings_5.species = None
    living_things_livingthings_5.article =  importer.locate_object(Article, "id", Article, "id", 176, {'id': 176, 'excerpt': 'Oryx', 'kicker': 'Oryx', 'content': '<p>Oryx is a genus consisting of four large antelope species called oryxes. Their pelage is pale with contrasting dark markings in the face and on the legs, and their long horns are almost straight. The exception is the scimitar oryx, which lacks dark markings on the legs, only has faint dark markings on the head, has an ochre neck, and has horns that are clearly decurved.</p>\r\n\r\n<p>Wikipediaより</p>\r\n\r\n<p>The Arabian oryx was only saved from extinction through a captive-breeding program and reintroduction to the wild.The scimitar oryx, which is now listed as extinct in the wild, also relies on a captive-breeding program for its survival.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:40:04+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:40:15.786088+00:00")} ) 
    living_things_livingthings_5.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 7, {'id': 7, 'name': 'living-things/each'} ) 
    living_things_livingthings_5 = importer.save_or_locate(living_things_livingthings_5)

    living_things_livingthings_6 = LivingThings()
    living_things_livingthings_6.name = 'オリックス'
    living_things_livingthings_6.slug = 'oryx-jp'
    living_things_livingthings_6.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_livingthings_6.habitat = None
    living_things_livingthings_6.species = None
    living_things_livingthings_6.article =  importer.locate_object(Article, "id", Article, "id", 177, {'id': 177, 'excerpt': 'オリックス', 'kicker': 'オリックス', 'content': '<p>オリックス</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:40:47+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:40:59.338420+00:00")} ) 
    living_things_livingthings_6.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 7, {'id': 7, 'name': 'living-things/each'} ) 
    living_things_livingthings_6 = importer.save_or_locate(living_things_livingthings_6)

    living_things_livingthings_7 = LivingThings()
    living_things_livingthings_7.name = 'Peacock'
    living_things_livingthings_7.slug = 'peacock'
    living_things_livingthings_7.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_livingthings_7.habitat = None
    living_things_livingthings_7.species = None
    living_things_livingthings_7.article =  importer.locate_object(Article, "id", Article, "id", 179, {'id': 179, 'excerpt': 'Peafowl', 'kicker': 'Peafowl', 'content': '<p>Peafowl is a common name for three bird species in the genera Pavo and Afropavo within the tribe Pavonini of the family Phasianidae, the pheasants and their allies. Male peafowl are referred to as peacocks, and female peafowl are referred to as peahens, even though peafowl of either sex are often referred to colloquially as &quot;peacocks&quot;.[1]</p>\r\n\r\n<p>The two Asiatic species are the blue or Indian peafowl originally of the Indian subcontinent, and the green peafowl of Southeast Asia; the one African species is the Congo peafowl, native only to the Congo Basin. Male peafowl are known for their piercing calls and their extravagant plumage. The latter is especially prominent in the Asiatic species, which have an eye-spotted &quot;tail&quot; or &quot;train&quot; of covert feathers, which they display as part of a courtship ritual.</p>\r\n\r\n<p>The functions of the elaborate iridescent colouration and large &quot;train&quot; of peacocks have been the subject of extensive scientific debate. Charles Darwin suggested that they served to attract females, and the showy features of the males had evolved by sexual selection. More recently, Amotz Zahavi proposed in his handicap theory that these features acted as honest signals of the males&#39; fitness, since less-fit males would be disadvantaged by the difficulty of surviving with such large and conspicuous structures.</p>\r\n\r\n<p>From Wikipedia</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:43:02+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:43:19.427300+00:00")} ) 
    living_things_livingthings_7.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 7, {'id': 7, 'name': 'living-things/each'} ) 
    living_things_livingthings_7 = importer.save_or_locate(living_things_livingthings_7)

    living_things_livingthings_8 = LivingThings()
    living_things_livingthings_8.name = 'クジャク'
    living_things_livingthings_8.slug = 'peacock-jp'
    living_things_livingthings_8.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_livingthings_8.habitat = None
    living_things_livingthings_8.species = None
    living_things_livingthings_8.article =  importer.locate_object(Article, "id", Article, "id", 178, {'id': 178, 'excerpt': 'クジャク', 'kicker': 'クジャク', 'content': '<p>クジャク</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T13:42:37+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T13:42:49.995760+00:00")} ) 
    living_things_livingthings_8.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 7, {'id': 7, 'name': 'living-things/each'} ) 
    living_things_livingthings_8 = importer.save_or_locate(living_things_livingthings_8)

    living_things_livingthings_9 = LivingThings()
    living_things_livingthings_9.name = 'Red Eyed Tree Frog'
    living_things_livingthings_9.slug = 'red-eyed-tree-frog'
    living_things_livingthings_9.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_livingthings_9.habitat = None
    living_things_livingthings_9.species = None
    living_things_livingthings_9.article =  importer.locate_object(Article, "id", Article, "id", 4782, {'id': 4782, 'excerpt': 'Red Eyed Tree Frog', 'kicker': 'Red Eyed Tree Frog', 'content': '<p>Agalychnis callidryas, or better known as the red-eyed tree frog, is an arboreal hylid native to Neotropical rainforests where it ranges from Mexico, through Central America, to Colombia. The scientific name of the red-eyed treefrog, A. callidryas, comes from the Greek words kalos (meaning &quot;beautiful&quot;) and dryas (a &quot;tree&quot; or &quot;wood nymph&quot;).</p>\r\n\r\n<p>This species has large, bright red eyes with vertically narrowed pupils. The red eyed tree frog is very colorful, with a vibrant green body, yellow and blue vertical stripes along its side, a white underside, brightly colored red or orange feet, and red eyes. Additionally, they have sticky pads on their toes that allow them to cling onto leaves . The skin on the red eyed treefrog&#39;s belly is soft and fragile, whereas the back is thicker and rougher. On average, the males are about two inches long, and the females are slightly bigger at around 3 inches.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-07-03T01:22:45+00:00"), 'updated_date': dateutil.parser.parse("2023-07-03T01:23:07.707602+00:00")} ) 
    living_things_livingthings_9.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 7, {'id': 7, 'name': 'living-things/each'} ) 
    living_things_livingthings_9 = importer.save_or_locate(living_things_livingthings_9)

    living_things_livingthings_10 = LivingThings()
    living_things_livingthings_10.name = 'アカメアマガエル'
    living_things_livingthings_10.slug = 'red-eyed-tree-frog-jp'
    living_things_livingthings_10.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_livingthings_10.habitat = None
    living_things_livingthings_10.species = None
    living_things_livingthings_10.article =  importer.locate_object(Article, "id", Article, "id", 4783, {'id': 4783, 'excerpt': 'アカメアマガエル', 'kicker': 'アカメアマガエル', 'content': '<p>アカメアマガエル</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-07-03T01:25:13+00:00"), 'updated_date': dateutil.parser.parse("2023-07-03T01:25:25.735057+00:00")} ) 
    living_things_livingthings_10.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 7, {'id': 7, 'name': 'living-things/each'} ) 
    living_things_livingthings_10 = importer.save_or_locate(living_things_livingthings_10)

    living_things_livingthings_11 = LivingThings()
    living_things_livingthings_11.name = 'Squirrel'
    living_things_livingthings_11.slug = 'squirrel'
    living_things_livingthings_11.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_livingthings_11.habitat = None
    living_things_livingthings_11.species = None
    living_things_livingthings_11.article =  importer.locate_object(Article, "id", Article, "id", 4784, {'id': 4784, 'excerpt': 'Squirrel', 'kicker': 'Squirrel', 'content': '<p>Squirrels are members of the family Sciuridae, a family that includes small or medium-size rodents. The squirrel family includes tree squirrels, ground squirrels (including chipmunks and prairie dogs, among others), and flying squirrels. Squirrels are indigenous to the Americas, Eurasia, and Africa, and were introduced by humans to Australia.[1] The earliest known fossilized squirrels date from the Eocene epoch, and among other living rodent families, the squirrels are most closely related to the mountain beaver and to the dormice.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-07-03T01:25:47+00:00"), 'updated_date': dateutil.parser.parse("2023-07-03T01:26:07.750674+00:00")} ) 
    living_things_livingthings_11.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 7, {'id': 7, 'name': 'living-things/each'} ) 
    living_things_livingthings_11 = importer.save_or_locate(living_things_livingthings_11)

    living_things_livingthings_12 = LivingThings()
    living_things_livingthings_12.name = 'リス'
    living_things_livingthings_12.slug = 'squirrel-jp'
    living_things_livingthings_12.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_livingthings_12.habitat = None
    living_things_livingthings_12.species = None
    living_things_livingthings_12.article =  importer.locate_object(Article, "id", Article, "id", 4785, {'id': 4785, 'excerpt': 'リス', 'kicker': 'リス', 'content': '', 'references': '<p>リス</p>', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-07-03T01:28:23+00:00"), 'updated_date': dateutil.parser.parse("2023-07-03T01:28:30.926830+00:00")} ) 
    living_things_livingthings_12.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 7, {'id': 7, 'name': 'living-things/each'} ) 
    living_things_livingthings_12 = importer.save_or_locate(living_things_livingthings_12)

    living_things_livingthings_13 = LivingThings()
    living_things_livingthings_13.name = 'Tiger'
    living_things_livingthings_13.slug = 'tiger'
    living_things_livingthings_13.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_livingthings_13.habitat = None
    living_things_livingthings_13.species = None
    living_things_livingthings_13.article =  importer.locate_object(Article, "id", Article, "id", 4786, {'id': 4786, 'excerpt': 'Tiger', 'kicker': 'Tiger', 'content': '<p>The tiger (Panthera tigris) is the largest living cat species and a member of the genus Panthera. It is most recognisable for its dark vertical stripes on orange fur with a white underside. An apex predator, it primarily preys on ungulates such as deer and wild boar. It is territorial and generally a solitary but social predator, requiring large contiguous areas of habitat, which support its requirements for prey and rearing of its offspring. Tiger cubs stay with their mother for about two years, then become independent and leave their mother&#39;s home range to establish their own.</p>\r\n\r\n<p>The tiger was first scientifically described in 1758 and once ranged widely from the Eastern Anatolia Region in the west to the Amur River basin in the east, and in the south from the foothills of the Himalayas to Bali in the Sunda Islands. Since the early 20th century, tiger populations have lost at least 93% of their historic range and have been extirpated from Western and Central Asia, the islands of Java and Bali, and in large areas of Southeast and South Asia and China. Today, the tiger&#39;s range is fragmented, stretching from Siberian temperate forests to subtropical and tropical forests on the Indian subcontinent, Indochina and Sumatra.</p>\r\n\r\n<p>The tiger is listed as Endangered on the IUCN Red List. As of 2015, the global wild tiger population was estimated to number between 3,062 and 3,948 mature individuals, with most of the populations living in small isolated pockets. India currently hosts the largest tiger population. Major reasons for population decline are habitat destruction, habitat fragmentation and poaching. Tigers are also victims of human&ndash;wildlife conflict, particularly in range countries with a high human population density.</p>\r\n\r\n<p>The tiger is among the most recognisable and popular of the world&#39;s charismatic megafauna. It featured prominently in the ancient mythology and folklore of cultures throughout its historic range, and continues to be depicted in modern films and literature, appearing on many flags, coats of arms and as mascots for sporting teams. The tiger is the national animal of India, Bangladesh, Malaysia and South Korea.</p>\r\n\r\n<p>From Wikipedia</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-07-03T01:29:08+00:00"), 'updated_date': dateutil.parser.parse("2023-07-03T01:29:19.979528+00:00")} ) 
    living_things_livingthings_13.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 7, {'id': 7, 'name': 'living-things/each'} ) 
    living_things_livingthings_13 = importer.save_or_locate(living_things_livingthings_13)

    living_things_livingthings_14 = LivingThings()
    living_things_livingthings_14.name = 'トラ'
    living_things_livingthings_14.slug = 'tiger-jp'
    living_things_livingthings_14.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_livingthings_14.habitat = None
    living_things_livingthings_14.species = None
    living_things_livingthings_14.article =  importer.locate_object(Article, "id", Article, "id", 4787, {'id': 4787, 'excerpt': 'トラ', 'kicker': 'トラ', 'content': '<p>The tiger (Panthera tigris) is the largest living cat species and a member of the genus Panthera. It is most recognisable for its dark vertical stripes on orange fur with a white underside. An apex predator, it primarily preys on ungulates such as deer and wild boar. It is territorial and generally a solitary but social predator, requiring large contiguous areas of habitat, which support its requirements for prey and rearing of its offspring. Tiger cubs stay with their mother for about two years, then become independent and leave their mother&#39;s home range to establish their own.</p>\r\n\r\n<p>The tiger was first scientifically described in 1758 and once ranged widely from the Eastern Anatolia Region in the west to the Amur River basin in the east, and in the south from the foothills of the Himalayas to Bali in the Sunda Islands. Since the early 20th century, tiger populations have lost at least 93% of their historic range and have been extirpated from Western and Central Asia, the islands of Java and Bali, and in large areas of Southeast and South Asia and China. Today, the tiger&#39;s range is fragmented, stretching from Siberian temperate forests to subtropical and tropical forests on the Indian subcontinent, Indochina and Sumatra.</p>\r\n\r\n<p>The tiger is listed as Endangered on the IUCN Red List. As of 2015, the global wild tiger population was estimated to number between 3,062 and 3,948 mature individuals, with most of the populations living in small isolated pockets. India currently hosts the largest tiger population. Major reasons for population decline are habitat destruction, habitat fragmentation and poaching. Tigers are also victims of human&ndash;wildlife conflict, particularly in range countries with a high human population density.</p>\r\n\r\n<p>The tiger is among the most recognisable and popular of the world&#39;s charismatic megafauna. It featured prominently in the ancient mythology and folklore of cultures throughout its historic range, and continues to be depicted in modern films and literature, appearing on many flags, coats of arms and as mascots for sporting teams. The tiger is the national animal of India, Bangladesh, Malaysia and South Korea.</p>\r\n\r\n<p>From Wikipedia</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-07-03T01:29:55+00:00"), 'updated_date': dateutil.parser.parse("2023-07-03T01:30:08.921647+00:00")} ) 
    living_things_livingthings_14.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 7, {'id': 7, 'name': 'living-things/each'} ) 
    living_things_livingthings_14 = importer.save_or_locate(living_things_livingthings_14)

    living_things_livingthings_15 = LivingThings()
    living_things_livingthings_15.name = 'Wolf'
    living_things_livingthings_15.slug = 'wolf'
    living_things_livingthings_15.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    living_things_livingthings_15.habitat = None
    living_things_livingthings_15.species = None
    living_things_livingthings_15.article =  importer.locate_object(Article, "id", Article, "id", 4788, {'id': 4788, 'excerpt': 'Wolf', 'kicker': 'Wolf', 'content': '<p>The wolf (Canis lupus[b]), also known as the gray wolf or grey wolf, is a large canine native to Eurasia and North America. More than thirty subspecies of Canis lupus have been recognized, and gray wolves, as popularly understood, comprise wild subspecies. The wolf is the largest extant member of the family Canidae. It is also distinguished from other Canis species by its less pointed ears and muzzle, as well as a shorter torso and a longer tail. The wolf is nonetheless related closely enough to smaller Canis species, such as the coyote and the golden jackal, to produce fertile hybrids with them. The banded fur of a wolf is usually mottled white, brown, gray, and black, although subspecies in the arctic region may be nearly all white.</p>\r\n\r\n<p>Of all members of the genus Canis, the wolf is most specialized for cooperative game hunting as demonstrated by its physical adaptations to tackling large prey, its more social nature, and its highly advanced expressive behaviour including individual or group howling. It travels in nuclear families consisting of a mated pair accompanied by their offspring. Offspring may leave to form their own packs on the onset of sexual maturity and in response to competition for food within the pack. Wolves are also territorial and fights over territory are among the principal causes of wolf mortality. The wolf is mainly a carnivore and feeds on large wild hooved mammals as well as smaller animals, livestock, carrion, and garbage. Single wolves or mated pairs typically have higher success rates in hunting than do large packs. Pathogens and parasites, notably rabies virus, may infect wolves.</p>\r\n\r\n<p>The global wild wolf population was estimated to be 300,000 in 2003 and is considered to be of Least Concern by the International Union for Conservation of Nature (IUCN). Wolves have a long history of interactions with humans, having been despised and hunted in most pastoral communities because of their attacks on livestock, while conversely being respected in some agrarian and hunter-gatherer societies. The wolf is also considered the ancestor of the domestic dog. Although the fear of wolves exists in many human societies, the majority of recorded attacks on people have been attributed to animals suffering from rabies. Wolf attacks on humans are rare because wolves are relatively few, live away from people, and have developed a fear of humans because of their experiences with hunters, ranchers, and shepherds.</p>\r\n\r\n<p>From Wikipedia</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-07-03T01:30:32+00:00"), 'updated_date': dateutil.parser.parse("2023-07-03T01:30:45.791073+00:00")} ) 
    living_things_livingthings_15.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 7, {'id': 7, 'name': 'living-things/each'} ) 
    living_things_livingthings_15 = importer.save_or_locate(living_things_livingthings_15)

    living_things_livingthings_16 = LivingThings()
    living_things_livingthings_16.name = 'オオカミ'
    living_things_livingthings_16.slug = 'wolf-jp'
    living_things_livingthings_16.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    living_things_livingthings_16.habitat = None
    living_things_livingthings_16.species = None
    living_things_livingthings_16.article =  importer.locate_object(Article, "id", Article, "id", 4789, {'id': 4789, 'excerpt': 'オオカミ', 'kicker': 'オオカミ', 'content': '<p>The wolf (Canis lupus[b]), also known as the gray wolf or grey wolf, is a large canine native to Eurasia and North America. More than thirty subspecies of Canis lupus have been recognized, and gray wolves, as popularly understood, comprise wild subspecies. The wolf is the largest extant member of the family Canidae. It is also distinguished from other Canis species by its less pointed ears and muzzle, as well as a shorter torso and a longer tail. The wolf is nonetheless related closely enough to smaller Canis species, such as the coyote and the golden jackal, to produce fertile hybrids with them. The banded fur of a wolf is usually mottled white, brown, gray, and black, although subspecies in the arctic region may be nearly all white.</p>\r\n\r\n<p>Of all members of the genus Canis, the wolf is most specialized for cooperative game hunting as demonstrated by its physical adaptations to tackling large prey, its more social nature, and its highly advanced expressive behaviour including individual or group howling. It travels in nuclear families consisting of a mated pair accompanied by their offspring. Offspring may leave to form their own packs on the onset of sexual maturity and in response to competition for food within the pack. Wolves are also territorial and fights over territory are among the principal causes of wolf mortality. The wolf is mainly a carnivore and feeds on large wild hooved mammals as well as smaller animals, livestock, carrion, and garbage. Single wolves or mated pairs typically have higher success rates in hunting than do large packs. Pathogens and parasites, notably rabies virus, may infect wolves.</p>\r\n\r\n<p>The global wild wolf population was estimated to be 300,000 in 2003 and is considered to be of Least Concern by the International Union for Conservation of Nature (IUCN). Wolves have a long history of interactions with humans, having been despised and hunted in most pastoral communities because of their attacks on livestock, while conversely being respected in some agrarian and hunter-gatherer societies. The wolf is also considered the ancestor of the domestic dog. Although the fear of wolves exists in many human societies, the majority of recorded attacks on people have been attributed to animals suffering from rabies. Wolf attacks on humans are rare because wolves are relatively few, live away from people, and have developed a fear of humans because of their experiences with hunters, ranchers, and shepherds.</p>\r\n\r\n<p>From Wikipedia</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-07-03T01:31:12+00:00"), 'updated_date': dateutil.parser.parse("2023-07-03T01:31:24.306961+00:00")} ) 
    living_things_livingthings_16.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 7, {'id': 7, 'name': 'living-things/each'} ) 
    living_things_livingthings_16 = importer.save_or_locate(living_things_livingthings_16)

    # Re-processing model: living_things.models.LivingThings

















