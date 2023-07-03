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
# manage.py dumpscript arts.PaintingMethod
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

    # Processing model: arts.models.PaintingMethod

    from arts.models import PaintingMethod

    arts_paintingmethod_1 = PaintingMethod()
    arts_paintingmethod_1.name = 'oil-painting'
    arts_paintingmethod_1.slug = 'oil-painting'
    arts_paintingmethod_1.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_paintingmethod_1.period = None
    arts_paintingmethod_1.location = None
    arts_paintingmethod_1.article =  importer.locate_object(Article, "id", Article, "id", 77, {'id': 77, 'excerpt': 'Oil painting', 'kicker': 'Oil painting', 'content': '<p>Oil painting is a type of fine art painting that uses pigments mixed with a medium of drying oil, such as linseed oil, to create a smooth, fluid consistency. It has been used for centuries to create some of the world&#39;s most famous works of art.</p>\r\n\r\n<p>Oil paintings are known for their luminous, vibrant colors and the ability to create rich, textured surfaces. The slow-drying nature of oil paint allows artists to make changes and corrections over time, making it a flexible and forgiving medium.</p>\r\n\r\n<p>The process of oil painting typically begins with a sketch or underpainting, which is then developed with layers of oil paint. Oil painters use a variety of techniques, such as glazing, impasto, and scumbling, to create depth and texture in their work.</p>\r\n\r\n<p>Oil painting can be a time-consuming process, as the slow-drying nature of the paint means that it can take days, or even weeks, for a painting to dry completely. However, the end result is often worth the wait, as the luminosity and depth of the colors are unmatched by other painting mediums.</p>\r\n\r\n<p>Whether you&#39;re a beginner or an experienced painter, oil painting can be a rewarding form of artistic expression. So gather your materials and start exploring the world of oil painting today!</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T06:03:55+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T06:06:44.839979+00:00")} ) 
    arts_paintingmethod_1.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 4, {'id': 4, 'name': 'arts/painting-methods'} ) 
    arts_paintingmethod_1 = importer.save_or_locate(arts_paintingmethod_1)

    arts_paintingmethod_2 = PaintingMethod()
    arts_paintingmethod_2.name = 'pastel-painting'
    arts_paintingmethod_2.slug = 'pastel-painting'
    arts_paintingmethod_2.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_paintingmethod_2.period = None
    arts_paintingmethod_2.location = None
    arts_paintingmethod_2.article =  importer.locate_object(Article, "id", Article, "id", 78, {'id': 78, 'excerpt': 'Pastel', 'kicker': 'Pastel', 'content': '<p>Pastel painting is a type of fine art painting that uses sticks of pigment in a dry, powdery form. Pastels come in a wide range of colors and can be used to create a variety of effects, from delicate washes of color to rich, velvety textures.</p>\r\n\r\n<p>Pastel paintings are known for their luminosity and the vibrancy of their colors. Unlike oil or acrylic paints, which are opaque, pastel pigments are transparent, which allows light to penetrate the surface and create a glowing effect.</p>\r\n\r\n<p>The process of pastel painting typically begins with a sketch or underpainting, which is then developed using pastel sticks. Pastel artists use a variety of techniques, such as layering, blending, and scumbling, to create depth and texture in their work.</p>\r\n\r\n<p>Pastel painting can be a challenging medium, as the dry pastel pigments can be easily smudged or rubbed away. However, with proper care and technique, pastel artists can create beautiful and long-lasting works of art.</p>\r\n\r\n<p>Whether you&#39;re a beginner or an experienced painter, pastel painting can be a fun and rewarding form of artistic expression. So grab your pastel sticks and start exploring the world of pastel painting today!</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T06:05:03+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T06:05:21.202840+00:00")} ) 
    arts_paintingmethod_2.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 4, {'id': 4, 'name': 'arts/painting-methods'} ) 
    arts_paintingmethod_2 = importer.save_or_locate(arts_paintingmethod_2)

    arts_paintingmethod_3 = PaintingMethod()
    arts_paintingmethod_3.name = 'watercolor-painting'
    arts_paintingmethod_3.slug = 'watercolor-painting'
    arts_paintingmethod_3.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_paintingmethod_3.period = None
    arts_paintingmethod_3.location = None
    arts_paintingmethod_3.article =  importer.locate_object(Article, "id", Article, "id", 79, {'id': 79, 'excerpt': 'Watercolor', 'kicker': 'Watercolor', 'content': '<p>Watercolor painting is a type of fine art painting that uses transparent watercolor pigments suspended in a water-based solution. The fluidity of the pigments and the water medium allow the artist to create soft, dreamy effects, and to blend and layer colors in unique ways. Watercolor paintings are often characterized by their luminous, transparent quality and the interplay of light and color.</p>\r\n\r\n<p>The process of watercolor painting typically begins with a sketch or underpainting, which is then developed and refined using a variety of watercolor techniques. Some common watercolor techniques include washes, dry brush work, and glazing, which involves laying down thin layers of color to create depth and dimension.</p>\r\n\r\n<p>Watercolor painting can be a challenging medium, as the pigments have a tendency to spread and bleed, making it difficult to control the final result. However, with practice and experimentation, watercolor artists can learn to harness these properties to create beautiful and expressive paintings.</p>\r\n\r\n<p>Whether you&#39;re a beginner or an experienced painter, watercolor painting can be a rewarding and fulfilling form of artistic expression. So grab your brush and watercolor palette, and start exploring the world of watercolor painting today!</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T06:06:04+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T06:06:16.304995+00:00")} ) 
    arts_paintingmethod_3.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 4, {'id': 4, 'name': 'arts/painting-methods'} ) 
    arts_paintingmethod_3 = importer.save_or_locate(arts_paintingmethod_3)

    arts_paintingmethod_4 = PaintingMethod()
    arts_paintingmethod_4.name = '油絵'
    arts_paintingmethod_4.slug = 'oil-painting-jp'
    arts_paintingmethod_4.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_paintingmethod_4.period = None
    arts_paintingmethod_4.location = None
    arts_paintingmethod_4.article =  importer.locate_object(Article, "id", Article, "id", 80, {'id': 80, 'excerpt': '', 'kicker': '', 'content': '<p className={pStyle}>\r\n            <span className={capDropStyle}></span>\r\n            油絵はファインアート絵画の一種で、顔料を亜麻仁油などの乾燥油の媒体に混ぜて、滑らかで流動性のある状態を作り出します。何世紀にもわたって、世界で最も有名な芸術作品の制作に使用されてきました。\r\n          </p>\r\n          <p className={pStyle}>\r\n            油絵は、その輝くような鮮やかな色彩と、豊かな質感の表面を作り出す能力で知られています。油絵具の乾燥が遅いため、アーティストが時間をかけて変更や修正を加えることができ、柔軟で寛容なメディウムとなっています。\r\n          </p>\r\n          <p className={pStyle}>\r\n            油絵のプロセスは、通常、スケッチや下絵から始まり、油絵具を何層にも重ねて発展させていきます。油絵画家は、作品の深みや質感を出すために、グレージング、インパスト、スキャンブルなど、さまざまな技法を用います。\r\n          </p>\r\n          <p className={pStyle}>\r\n            油絵は絵の具の乾燥が遅いため、完全に乾くまで何日も、あるいは何週間もかかることもあり、時間のかかる作業となります。しかし、その色の輝きと深みは他の画材では得られないものであり、待つだけの価値がある場合が多いのです。\r\n          </p>\r\n          <p className={pStyle}>\r\n            初心者でも経験者でも、油絵は実りある芸術表現になるはずです。さっそく材料を揃えて、油絵の世界に挑戦してみましょう。\r\n          </p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T06:07:04+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T06:07:31.544017+00:00")} ) 
    arts_paintingmethod_4.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 4, {'id': 4, 'name': 'arts/painting-methods'} ) 
    arts_paintingmethod_4 = importer.save_or_locate(arts_paintingmethod_4)

    arts_paintingmethod_5 = PaintingMethod()
    arts_paintingmethod_5.name = '水彩画'
    arts_paintingmethod_5.slug = 'pastel-painting-jp'
    arts_paintingmethod_5.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_paintingmethod_5.period = None
    arts_paintingmethod_5.location = None
    arts_paintingmethod_5.article =  importer.locate_object(Article, "id", Article, "id", 81, {'id': 81, 'excerpt': 'パステル画', 'kicker': 'パステル画', 'content': '<p>パステル画は、乾燥した粉状の顔料をスティック状にしたものを使用するファインアートペインティングの一種です。パステルにはさまざまな色があり、繊細な色調から豊かでベルベットのような質感まで、さまざまな効果を生み出すために使用することができます。</p>\r\n\r\n<p>パステル画は、その輝きと色彩の鮮やかさで知られています。油絵具やアクリル絵具が不透明であるのとは異なり、パステル顔料は透明であるため、光を透過して輝くような効果を生み出します。</p>\r\n\r\n<p>パステル画のプロセスは、通常、スケッチや下絵から始まり、パステルスティックを使って展開されます。パステル画家は、重ねたり、混ぜたり、こすったりといったさまざまな技法を用いて、作品に深みと質感を作り出します。</p>\r\n\r\n<p>パステル画は、乾燥したパステル顔料が簡単に滲んだりこすれたりするため、難しい画材と言えます。しかし、適切なケアとテクニックがあれば、パステル アーティストは、美しく長持ちする作品を作ることができます。</p>\r\n\r\n<p>初心者でも経験者でも、パステル画は楽しくてやりがいのある芸術表現になります。</p>\r\n\r\n<p>パステル画は、初心者でも経験者でも、楽しくて実りのある芸術表現です。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T06:07:57+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T06:08:06.222322+00:00")} ) 
    arts_paintingmethod_5.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 4, {'id': 4, 'name': 'arts/painting-methods'} ) 
    arts_paintingmethod_5 = importer.save_or_locate(arts_paintingmethod_5)

    arts_paintingmethod_6 = PaintingMethod()
    arts_paintingmethod_6.name = '水彩画'
    arts_paintingmethod_6.slug = 'watercolor-painting-jp'
    arts_paintingmethod_6.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_paintingmethod_6.period = None
    arts_paintingmethod_6.location = None
    arts_paintingmethod_6.article =  importer.locate_object(Article, "id", Article, "id", 82, {'id': 82, 'excerpt': '水彩画', 'kicker': '水彩画', 'content': '<p>水彩画は、水性溶液に懸濁させた透明な水彩顔料を使用するファインアート絵画の一種です。顔料と水性媒体の流動性により、柔らかく夢のような効果を生み出し、ユニークな方法で色を混ぜたり重ねたりすることができます。水彩画はしばしば、その発光性、透明性、光と色の相互作用によって特徴付けられます。</p>\r\n\r\n<p>水彩画のプロセスは通常、スケッチや下絵から始まり、様々な水彩画の技法を用いて発展・洗練させていきます。水彩画の一般的な技法には、ウォッシュ、ドライブラシ、グレージングなどがあり、薄く色を重ねて深みと奥行きを出すことができます。</p>\r\n\r\n<p>水彩画は、顔料が広がったりにじんだりする傾向があるため、最終的な仕上がりをコントロールすることが難しい画材です。しかし、練習と実験を重ねることで、水彩画家はその特性を生かして美しく表現豊かな絵画を描くことができるようになります。</p>\r\n\r\n<p>初心者でも経験者でも、水彩画はやりがいのある、充実した芸術表現になります。さっそく筆と水彩パレットを持って、水彩画の世界を探求してみてください。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T06:09:32+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T06:09:58.124230+00:00")} ) 
    arts_paintingmethod_6.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 4, {'id': 4, 'name': 'arts/painting-methods'} ) 
    arts_paintingmethod_6 = importer.save_or_locate(arts_paintingmethod_6)

    # Re-processing model: arts.models.PaintingMethod







