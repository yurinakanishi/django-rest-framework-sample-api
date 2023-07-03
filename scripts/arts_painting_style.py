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
# manage.py dumpscript arts.PaintingStyle
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

    # Processing model: arts.models.PaintingStyle

    from arts.models import PaintingStyle

    arts_paintingstyle_1 = PaintingStyle()
    arts_paintingstyle_1.name = 'abstract-styles'
    arts_paintingstyle_1.slug = 'abstract-styles'
    arts_paintingstyle_1.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_paintingstyle_1.period = None
    arts_paintingstyle_1.location = None
    arts_paintingstyle_1.article =  importer.locate_object(Article, "id", Article, "id", 83, {'id': 83, 'excerpt': 'A bstract art', 'kicker': 'A bstract art', 'content': '<p>A bstract art is a form of art that is not representational. This means that the artist does not attempt to create a work of art that accurately represents the external world. Instead, the artist focuses on the shapes, colors, and textures of the work itself.</p>\r\n\r\n<p>Some of the earliest abstract art was created by the Impressionist artists in the late 1800s. These artists were interested in capturing the momentary effects of light and color, and they often created paintings that were not easily identifiable as objects. In the early 1900s, the Cubist artists took abstract art a step further by creating paintings that were composed of multiple viewpoints and angles.</p>\r\n\r\n<p>Abstract art continued to evolve in the mid-20th century, when artists like Jackson Pollock began to experiment with non-traditional painting techniques. Pollock is famous for his &quot;drip paintings,&quot; which involved dripping paint onto a canvas from a stick or brush. Other artists of this era began to create art that was inspired by the natural world, but was not meant to be a literal representation of it.</p>\r\n\r\n<p>Today, abstract art is still widely popular and can be found in galleries and museums all over the world. Some of the most famous abstract artists include Claude Monet, Pablo Picasso, and Wassily Kandinsky.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T06:56:50+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T06:59:36.428687+00:00")} ) 
    arts_paintingstyle_1.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_1 = importer.save_or_locate(arts_paintingstyle_1)

    arts_paintingstyle_2 = PaintingStyle()
    arts_paintingstyle_2.name = '抽象派'
    arts_paintingstyle_2.slug = 'abstract-styles-jp'
    arts_paintingstyle_2.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_paintingstyle_2.period = None
    arts_paintingstyle_2.location = None
    arts_paintingstyle_2.article =  importer.locate_object(Article, "id", Article, "id", 84, {'id': 84, 'excerpt': '抽象芸術', 'kicker': '抽象芸術', 'content': '<p>抽象芸術は、表象的ではない芸術の形態である。これは、芸術家が外部の世界を正確に表現する芸術作品を作ろうとするのではなく、その作品自体の形、色、質感に焦点を当てることを意味する。</p>\r\n\r\n<p>最も初期の抽象芸術のいくつかは、1800年代後半に印象派の芸術家によって作成された。これらの芸術家は、光と色の瞬間的な効果を捉えることに関心があり、容易に物体として識別できない絵画を作成することが多かった。1900年代初頭に、キュービズムの芸術家は、抽象芸術をさらに一歩進めて、複数の視点と角度で構成された絵画を作成した。</p>\r\n\r\n<p>抽象芸術は20世紀半ばに進化を続け、ジャクソン・ポロックのような芸術家が非伝統的な絵画技法の実験を始めた。ポロックは、棒や筆からキャンバスに絵の具を垂らす「ドリップペインティング」で有名である。この時代の他の芸術家たちは、自然界に触発された芸術を創造し始めたが、それは文字通りの表現ではなかった。</p>\r\n\r\n<p>今日、抽象芸術は依然として広く人気があり、世界中のギャラリーや博物館で見ることができます。最も有名な抽象芸術家には、クロード・モネ、パブロ・ピカソ、ワシリー・カンディンスキーなどがいます。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T06:58:47+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T06:59:04.175853+00:00")} ) 
    arts_paintingstyle_2.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_2 = importer.save_or_locate(arts_paintingstyle_2)

    arts_paintingstyle_3 = PaintingStyle()
    arts_paintingstyle_3.name = 'chinese-style'
    arts_paintingstyle_3.slug = 'chinese-style'
    arts_paintingstyle_3.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_paintingstyle_3.period = None
    arts_paintingstyle_3.location = None
    arts_paintingstyle_3.article =  importer.locate_object(Article, "id", Article, "id", 85, {'id': 85, 'excerpt': 'Chinese', 'kicker': 'Chinese', 'content': '<p>Chinese art is the product of the Eastern Han Dynasty period, and is one of the oldest continuous traditions in the world. A new form of art called &ldquo;xieyi&rdquo; (literally meaning &ldquo;to paint objects&rdquo;) appeared during this time. Unlike the traditional art of &ldquo;yihua&rdquo; which focused on calligraphy and landscape painting, xieyi emphasized the depiction of objects and scenes from everyday life. This new form of art would go on to become the foundation of all traditional Chinese art forms.</p>\r\n\r\n<p>During the Tang Dynasty period, Chinese art reached its peak. Notable artists of the era include Wu Daozi, whose paintings depicted scenes of a lively and colorful nature, and Zhang Xuan, who is considered the father of Chinese painting. Zhang&#39;s work is characterized by its elegant and subtle use of color.</p>\r\n\r\n<p>During the Ming Dynasty period, Chinese art underwent a gradual transformation. Artists of the period began to experiment with new techniques and styles, resulting in a more diverse and eclectic body of work. One of the most famous artists of the period is Wang Shimin, whose paintings are noted for their striking use of color and delicate brushstrokes.</p>\r\n\r\n<p>Today, Chinese art is considered to be one of the most important and influential art traditions in the world. It has had a profound impact on the development of art in countries all around the world.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:12:18+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:12:37.795012+00:00")} ) 
    arts_paintingstyle_3.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_3 = importer.save_or_locate(arts_paintingstyle_3)

    arts_paintingstyle_4 = PaintingStyle()
    arts_paintingstyle_4.name = '中国画'
    arts_paintingstyle_4.slug = 'chinese-style-jp'
    arts_paintingstyle_4.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_paintingstyle_4.period = None
    arts_paintingstyle_4.location = None
    arts_paintingstyle_4.article =  importer.locate_object(Article, "id", Article, "id", 86, {'id': 86, 'excerpt': '中国', 'kicker': '中国', 'content': '<p>中国の芸術は東漢時代の産物であり、世界で最も古くから続く伝統の一つである。この時代に、「xieyi」(文字通り「物を描く」という意味)と呼ばれる新しい芸術が出現した。書や風景画を中心とした伝統芸術の「義華」とは異なり、xieyiは日常生活の中の物や風景の描写を重視した。この新しい芸術は、中国の伝統芸術の基礎となった。</p>\r\n\r\n<p>唐の時代、中国の芸術は最盛期を迎えました。この時代の著名な画家には、生き生きとした色彩豊かな自然の風景を描いた呉道玄や、中国絵画の父とされる張萱などがいます。張の作品は、優雅で繊細な色彩使いが特徴です。</p>\r\n\r\n<p>明代になると、中国の芸術は徐々に変化した。この時代の芸術家たちは新しい技術やスタイルを試し始め、その結果、より多様で折衷的な作品が生まれた。この時代の最も有名な芸術家の一人は王時敏で、彼の絵は色の鮮やかさと繊細な筆法で知られている。</p>\r\n\r\n<p>今日、中国の芸術は世界で最も重要で影響力のある芸術の伝統の一つと考えられており、世界中の国々の芸術の発展に大きな影響を与えてきました。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:12:56+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:13:12.749639+00:00")} ) 
    arts_paintingstyle_4.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_4 = importer.save_or_locate(arts_paintingstyle_4)

    arts_paintingstyle_5 = PaintingStyle()
    arts_paintingstyle_5.name = 'cubism'
    arts_paintingstyle_5.slug = 'cubism'
    arts_paintingstyle_5.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_paintingstyle_5.period = None
    arts_paintingstyle_5.location = None
    arts_paintingstyle_5.article =  importer.locate_object(Article, "id", Article, "id", 87, {'id': 87, 'excerpt': 'Cubism', 'kicker': 'Cubism', 'content': '<p>Cubism is an early-20th century avant-garde art movement that pioneered the use of geometric forms in painting and sculpture. Cubism has been called the most influential art movement of the 20th century.</p>\r\n\r\n<p>The cubists sought to break down the barriers between different art media, and to flatten the appearance of objects in order to show the multiple perspectives of an object from all angles simultaneously. In painting, this was done by using geometric shapes to create a two-dimensional picture that showed the object from multiple angles at the same time.</p>\r\n\r\n<p>The cubist artists included Georges Braque, Pablo Picasso, Juan Gris, Fernand L&eacute;ger, and Robert Delaunay. Their work was exhibited in Paris in the early 1910s, and their influence was soon felt around the world.</p>\r\n\r\n<p>Cubism is often seen as the beginning of the modern art movement, and it has been credited with influencing a wide range of later artistic movements, including futurism, constructivism, and De Stijl.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:17:08+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:17:33.009714+00:00")} ) 
    arts_paintingstyle_5.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_5 = importer.save_or_locate(arts_paintingstyle_5)

    arts_paintingstyle_6 = PaintingStyle()
    arts_paintingstyle_6.name = 'キュビズム'
    arts_paintingstyle_6.slug = 'cubism-jp'
    arts_paintingstyle_6.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_paintingstyle_6.period = None
    arts_paintingstyle_6.location = None
    arts_paintingstyle_6.article =  importer.locate_object(Article, "id", Article, "id", 88, {'id': 88, 'excerpt': 'キュービズム', 'kicker': 'キュービズム', 'content': '<p>キュービズムは、20世紀初頭のアバンギャルドなArt Movementで、絵画や彫刻に幾何学的な形を使用する先駆者となった。キュービズムは、20世紀の最も影響力のあるArt Movementと呼ばれている。</p>\r\n\r\n<p>キュービズムは、異なる芸術媒体間の障壁を打破し、あらゆる角度からの物体の複数の視点を同時に示すために、物体の外観を平坦にしようとした。絵画では、幾何学的な形状を使用して、物体を複数の角度から同時に示す2次元の絵を作成することによって、これが行われた。</p>\r\n\r\n<p>キュービズムの芸術家には、ジョルジュ・ブラック、パブロ・ピカソ、フアン・グリス、フェルナン・レジェ、ロベール・ドローネーなどがいる。彼らの作品は1910年代初頭にパリで展示され、その影響はすぐに世界中に感じられた。</p>\r\n\r\n<p>キュービズムは現代Art Movementの始まりと見なされることが多く、未来主義、構成主義、De Stijlなど、その後の幅広い芸術運動に影響を与えたとされています。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:18:29+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:18:43.224923+00:00")} ) 
    arts_paintingstyle_6.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_6 = importer.save_or_locate(arts_paintingstyle_6)

    arts_paintingstyle_7 = PaintingStyle()
    arts_paintingstyle_7.name = 'expressionism'
    arts_paintingstyle_7.slug = 'expressionism'
    arts_paintingstyle_7.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_paintingstyle_7.period = None
    arts_paintingstyle_7.location = None
    arts_paintingstyle_7.article =  importer.locate_object(Article, "id", Article, "id", 89, {'id': 89, 'excerpt': 'Expressionism', 'kicker': 'Expressionism', 'content': '<p>Expressionism is a movement in the arts that stresses emotional intensity and artist&#39;s personal interpretation over traditional aesthetics. It began in the early 20th century as an offshoot of realism, but eventually developed its own distinct style. The main Expressionist artists were painters, but the movement also included poetry, music, and theater.</p>\r\n\r\n<p>Expressionism began in Germany, where the artists were reacting to the rapid changes brought about by modernization. They wanted to express their feelings about the world in their art, rather than simply depict it objectively. To do this, they often used distorted shapes and intense colors, as well as emotional and symbolic subject matter.</p>\r\n\r\n<p>One of the earliest and most famous Expressionist paintings is The Scream by Edvard Munch. This work features a figure with an agonized expression, set against a bright orange background. Other well-known Expressionist artists include Vincent van Gogh, Ernst Ludwig Kirchner, and Oskar Kokoschka.</p>\r\n\r\n<p>In the early years, Expressionism was met with a great deal of skepticism and was not initially embraced by the art establishment. However, it eventually came to be recognized as a major movement and had a significant impact on later art movements such as abstract expressionism.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:27:55+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:28:08.002805+00:00")} ) 
    arts_paintingstyle_7.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_7 = importer.save_or_locate(arts_paintingstyle_7)

    arts_paintingstyle_8 = PaintingStyle()
    arts_paintingstyle_8.name = '表現主義'
    arts_paintingstyle_8.slug = 'expressionism-jp'
    arts_paintingstyle_8.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_paintingstyle_8.period = None
    arts_paintingstyle_8.location = None
    arts_paintingstyle_8.article =  importer.locate_object(Article, "id", Article, "id", 90, {'id': 90, 'excerpt': '表現主義', 'kicker': '表現主義', 'content': '<p>表現主義は、伝統的な美学よりも感情的な強さと芸術家の個人的な解釈を強調する芸術の運動です。20世紀初頭にリアリズムの副産物として始まりましたが、最終的に独自のスタイルを開発しました。表現主義の主な芸術家は画家でしたが、この運動には詩、音楽、演劇も含まれていました。</p>\r\n\r\n<p>表現主義は、近代化によってもたらされた急速な変化に対応していたドイツで始まりました。彼らは、世界を単に客観的に描写するのではなく、芸術の中で世界に対する感情を表現したいと考えていました。そのために、彼らはしばしば歪んだ形と強烈な色、そして感情的で象徴的な主題を使用しました。</p>\r\n\r\n<p>最も初期の最も有名な表現主義の絵画の1つは、エドヴァルド・ムンクの「叫び」です。この作品は、明るいオレンジ色の背景に苦悶した表情の人物を描いています。他の有名な表現主義の芸術家には、フィンセント・ファン・ゴッホ、エルンスト・ルートヴィッヒ・キルヒナー、オスカー・ココシュカなどがいます。</p>\r\n\r\n<p>当初、表現主義は芸術界から大きな懐疑の目を向けられ、受け入れられなかったが、やがて大きな運動として認識されるようになり、抽象表現主義などのその後の芸術運動に大きな影響を与えた。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:29:00+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:29:13.141022+00:00")} ) 
    arts_paintingstyle_8.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_8 = importer.save_or_locate(arts_paintingstyle_8)

    arts_paintingstyle_9 = PaintingStyle()
    arts_paintingstyle_9.name = 'impressionism'
    arts_paintingstyle_9.slug = 'impressionism'
    arts_paintingstyle_9.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_paintingstyle_9.period = None
    arts_paintingstyle_9.location = None
    arts_paintingstyle_9.article =  importer.locate_object(Article, "id", Article, "id", 91, {'id': 91, 'excerpt': 'Impressionism', 'kicker': 'Impressionism', 'content': '<p>Impressionism is a form of art that was popularized in the mid-19th century. The term impressionism is derived from the French word impression, which means &quot;to give an impression.&quot; The impressionist movement began in the early 1870s with a group of Paris-based artists who rejected traditional art techniques in favor of capturing the momentary effects of natural light and color.</p>\r\n\r\n<p>Impressionist artists sought to capture the essence of a scene, rather than create a precise replica. They often painted outdoors, and used short brushstrokes and a limited color palette to capture the transient effects of sunlight and atmosphere. Impressionist paintings are typically characterized by an open composition, a lack of precise detail, and a focus on light and color.</p>\r\n\r\n<p>The Impressionist movement was initially met with criticism from the art establishment. However, the movement grew in popularity and by the 1880s, Impressionist paintings were being exhibited in some of the world&#39;s most prestigious museums. Today, Impressionist paintings are among the most popular and highly-valued works of art in the world.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:29:58+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:30:50.242509+00:00")} ) 
    arts_paintingstyle_9.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_9 = importer.save_or_locate(arts_paintingstyle_9)

    arts_paintingstyle_10 = PaintingStyle()
    arts_paintingstyle_10.name = '印象派'
    arts_paintingstyle_10.slug = 'impressionism-jp'
    arts_paintingstyle_10.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_paintingstyle_10.period = None
    arts_paintingstyle_10.location = None
    arts_paintingstyle_10.article =  importer.locate_object(Article, "id", Article, "id", 92, {'id': 92, 'excerpt': '印象派', 'kicker': '印象派', 'content': '<p>印象派は、19世紀半ばに大衆化した芸術です。印象派という言葉は、「印象を与える」という意味のフランス語のimpressionに由来しています。印象派の運動は、1870年代初頭にパリを拠点とする芸術家のグループによって始まりました。彼らは、伝統的な芸術技術を拒否し、自然光と色の瞬間的な効果を捉えることを好みました。</p>\r\n\r\n<p>印象派の芸術家は、正確なレプリカを作成するのではなく、シーンの本質を捉えようとしました。彼らはしばしば屋外で絵を描き、短いブラシストロークと限られたカラーパレットを使用して、日光と大気の一時的な効果を捉えました。印象派の絵画は、一般的に、開放的な構成、正確な詳細の欠如、光と色への焦点によって特徴づけられる。</p>\r\n\r\n<p>印象派の運動は当初、芸術界からの批判にさらされました。しかし、この運動は人気を博し、1880年代までには、印象派の絵画が世界で最も権威のある博物館のいくつかで展示されるようになりました。今日、印象派の絵画は、世界で最も人気があり、高く評価されている芸術作品の1つです。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:31:37+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:31:52.784445+00:00")} ) 
    arts_paintingstyle_10.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_10 = importer.save_or_locate(arts_paintingstyle_10)

    arts_paintingstyle_11 = PaintingStyle()
    arts_paintingstyle_11.name = 'indian-style'
    arts_paintingstyle_11.slug = 'indian-style'
    arts_paintingstyle_11.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_paintingstyle_11.period = None
    arts_paintingstyle_11.location = None
    arts_paintingstyle_11.article =  importer.locate_object(Article, "id", Article, "id", 93, {'id': 93, 'excerpt': 'indian', 'kicker': 'indian', 'content': '<p>The Indian art style is one of the most unique and intricate in the world. With its origins in the ancient Hindu, Buddhist and Jain religious art, Indian art has evolved over the centuries to incorporate a wide range of regional and local styles. The Hindu art style is characterized by its use of bright colors and its focus on religious themes, while the Buddhist art style is typically characterized by its use of monochrome palettes and its focus on spiritual concepts.</p>\r\n\r\n<p>The Indian art style is known for its intricate designs and its use of a wide range of colors. The art is often very detailed, with a focus on religious themes and spiritual concepts. The art style is also known for its use of ornamentation, with a focus on intricate designs and patterns.</p>\r\n\r\n<p>The Indian art style is found in a variety of different mediums, including painting, sculpture, architecture, and textiles. The art is often very colorful, with a focus on bright and vibrant colors. The art is also often very intricate, with a focus on intricate designs and patterns.</p>\r\n\r\n<p>The Indian art style is found in a variety of different forms, including painting, sculpture, architecture, and textiles. The art is often very colorful, with a focus on bright and vibrant colors. The art is also often very intricate, with a focus on intricate designs and patterns.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:32:23+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:33:10.621084+00:00")} ) 
    arts_paintingstyle_11.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_11 = importer.save_or_locate(arts_paintingstyle_11)

    arts_paintingstyle_12 = PaintingStyle()
    arts_paintingstyle_12.name = 'インド画'
    arts_paintingstyle_12.slug = 'indian-style-jp'
    arts_paintingstyle_12.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_paintingstyle_12.period = None
    arts_paintingstyle_12.location = None
    arts_paintingstyle_12.article =  importer.locate_object(Article, "id", Article, "id", 94, {'id': 94, 'excerpt': 'インド', 'kicker': 'インド', 'content': '<p>インドの芸術スタイルは、世界で最もユニークで複雑なものの1つです。古代のヒンドゥー教、仏教、ジャイナ教の宗教芸術を起源とするインドの芸術は、何世紀にもわたって進化し、地域や地方の幅広いスタイルを取り入れてきました。ヒンドゥー教の芸術スタイルは、明るい色を使用し、宗教的なテーマに焦点を当てていることが特徴です。一方、仏教の芸術スタイルは、典型的には、モノクロのパレットを使用し、精神的な概念に焦点を当てていることが特徴です。</p>\r\n\r\n<p>インドの芸術スタイルは、その複雑なデザインと幅広い色の使用で知られています。その芸術はしばしば非常に詳細で、宗教的なテーマと精神的な概念に焦点が当てられています。その芸術スタイルはまた、複雑なデザインとパターンに焦点を当てた装飾の使用でも知られています。</p>\r\n\r\n<p>インドの芸術スタイルは、絵画、彫刻、建築、織物など、さまざまな媒体に見られる。芸術はしばしば非常にカラフルで、明るく鮮やかな色に焦点が当てられている。芸術はまた、しばしば非常に複雑で、複雑なデザインやパターンに焦点が当てられている。</p>\r\n\r\n<p>インドの芸術スタイルには、絵画、彫刻、建築、織物など、さまざまな形があります。芸術はしばしば非常にカラフルで、明るく鮮やかな色に焦点が当てられています。芸術はまた、しばしば非常に複雑で、複雑なデザインやパターンに焦点が当てられています。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:33:38+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:34:15.651321+00:00")} ) 
    arts_paintingstyle_12.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_12 = importer.save_or_locate(arts_paintingstyle_12)

    arts_paintingstyle_13 = PaintingStyle()
    arts_paintingstyle_13.name = 'japanese-style'
    arts_paintingstyle_13.slug = 'japanese-style'
    arts_paintingstyle_13.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_paintingstyle_13.period = None
    arts_paintingstyle_13.location = None
    arts_paintingstyle_13.article =  importer.locate_object(Article, "id", Article, "id", 95, {'id': 95, 'excerpt': 'Japanese', 'kicker': 'Japanese', 'content': '<p>The Japanese style of arts is a term used to describe the unique and distinctively Japanese approach to the visual arts. This approach is characterized by a focus on simplicity, minimalism, and the use of natural materials.</p>\r\n\r\n<p>One of the most important aspects of Japanese art is the emphasis on simplicity and minimalism. This is reflected in the use of basic shapes and lines, and the lack of ornamentation. In addition, the use of natural materials is another hallmark of Japanese art. This can be seen in the use of wood, paper, and fabric, all of which are used in a simple and unpretentious way.</p>\r\n\r\n<p>The Japanese style of art is also characterized by a focus on the elements of nature. This can be seen in the use of landscapes and flowers in art, as well as the use of light and shadow. In addition, the Japanese have a strong appreciation for the beauty of simplicity, which is reflected in their art.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:35:27+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:35:42.143936+00:00")} ) 
    arts_paintingstyle_13.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_13 = importer.save_or_locate(arts_paintingstyle_13)

    arts_paintingstyle_14 = PaintingStyle()
    arts_paintingstyle_14.name = '日本画'
    arts_paintingstyle_14.slug = 'japanese-style-jp'
    arts_paintingstyle_14.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_paintingstyle_14.period = None
    arts_paintingstyle_14.location = None
    arts_paintingstyle_14.article =  importer.locate_object(Article, "id", Article, "id", 96, {'id': 96, 'excerpt': '日本式', 'kicker': '日本式', 'content': '<p>日本式の芸術とは、シンプルさ、ミニマリズム、自然素材の使用に重点を置いた、日本独自の視覚芸術へのアプローチを表す用語です。</p>\r\n\r\n<p>日本の芸術の最も重要な側面の1つは、シンプルさとミニマリズムに重点を置いていることです。これは、基本的な形や線の使用、装飾の欠如に反映されています。また、自然素材の使用は、日本の芸術のもう1つの特徴です。これは、木、紙、布の使用に見られますが、これらはすべてシンプルで気取らない方法で使用されています。</p>\r\n\r\n<p>また、日本の芸術は、風景や花、光や影など、自然の要素を重視することに特徴があります。また、日本人は、簡素さの美しさを強く認識しており、それが芸術に反映されています。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:36:09+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:36:22.673493+00:00")} ) 
    arts_paintingstyle_14.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_14 = importer.save_or_locate(arts_paintingstyle_14)

    arts_paintingstyle_15 = PaintingStyle()
    arts_paintingstyle_15.name = 'modernism'
    arts_paintingstyle_15.slug = 'modernism'
    arts_paintingstyle_15.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_paintingstyle_15.period = None
    arts_paintingstyle_15.location = None
    arts_paintingstyle_15.article =  importer.locate_object(Article, "id", Article, "id", 97, {'id': 97, 'excerpt': 'Modernism', 'kicker': 'Modernism', 'content': '<p>What is Modernism?</p>\r\n\r\n<p>Modernism is a term used to describe the era that began with the Industrial Revolution and ended with World War II. The term is also used to describe the art and architecture that developed during this period. Art and architecture were no longer constrained by the rules of the past. Artists and architects were free to experiment and create new styles.</p>\r\n\r\n<p>The Art of Modernism</p>\r\n\r\n<p>The art of modernism is characterized by its abstraction and its lack of realism. Artists abandoned the traditional methods of painting and sculpting and began to experiment with new techniques and media. They also began to experiment with new subjects and new styles.</p>\r\n\r\n<p>One of the most famous modernist painters is Pablo Picasso. Picasso was a pioneer of cubism, a style of painting that was characterized by its abstract, geometric forms. Other famous modernist painters include Vincent van Gogh, Frida Kahlo, and Jackson Pollock.</p>\r\n\r\n<p>The Architecture of Modernism</p>\r\n\r\n<p>The architecture of modernism is characterized by its use of geometric shapes and its rejection of traditional styles. Architects abandoned the use of columns and arches and began to use steel and concrete to create new and innovative shapes.</p>\r\n\r\n<p>One of the most famous modernist architects is Frank Lloyd Wright. Wright was a pioneer of the Prairie Style of architecture, which was characterized by its use of simple, geometric shapes. Other famous modernist architects include Walter Gropius, Ludwig Mies van der Rohe, and Le Corbusier.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:48:50+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:49:20.094360+00:00")} ) 
    arts_paintingstyle_15.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_15 = importer.save_or_locate(arts_paintingstyle_15)

    arts_paintingstyle_16 = PaintingStyle()
    arts_paintingstyle_16.name = 'モダニズム'
    arts_paintingstyle_16.slug = 'modernism-jp'
    arts_paintingstyle_16.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_paintingstyle_16.period = None
    arts_paintingstyle_16.location = None
    arts_paintingstyle_16.article =  importer.locate_object(Article, "id", Article, "id", 98, {'id': 98, 'excerpt': 'モダニズム', 'kicker': 'モダニズム', 'content': '<p>モダニズムとは何ですか?</p>\r\n\r\n<p>モダニズムとは、産業革命に始まり、第二次世界大戦で終わった時代を表す言葉です。また、この時代に発展した芸術や建築を表す言葉でもあります。芸術や建築は、もはや過去のルールに縛られることはありませんでした。芸術家や建築家は、自由に新しいスタイルを実験し、創造することができました。</p>\r\n\r\n<p>モダニズムの芸術</p>\r\n\r\n<p>モダニズムの芸術は、その抽象性とリアリズムの欠如によって特徴づけられます。芸術家は、伝統的な絵画や彫刻の方法を捨てて、新しい技術やメディアを試し始めました。また、新しい主題や新しいスタイルを試し始めました。</p>\r\n\r\n<p>最も有名なモダニズム画家の一人はパブロ・ピカソです。ピカソは、抽象的で幾何学的な形を特徴とする絵画様式であるキュービズムの先駆者でした。他の有名なモダニズム画家には、フィンセント・ファン・ゴッホ、フリーダ・カーロ、ジャクソン・ポロックなどがいます。</p>\r\n\r\n<p>モダニズムの建築</p>\r\n\r\n<p>モダニズムの建築は、幾何学的な形を使用し、従来のスタイルを拒否することが特徴です。建築家たちは柱やアーチの使用をやめ、新しく革新的な形を作るために鋼やコンクリートを使い始めました。</p>\r\n\r\n<p>最も有名なモダニズム建築家の一人はフランク・ロイド・ライトです。ライトは、単純な幾何学的な形を使用することを特徴とするプレーリー様式の建築の先駆者でした。他の有名なモダニズム建築家には、ヴァルター・グロピウス、ルートヴィヒ・ミース・ファン・デル・ローエ、ル・コルビュジエなどがいます。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:49:52+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:50:30.763437+00:00")} ) 
    arts_paintingstyle_16.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_16 = importer.save_or_locate(arts_paintingstyle_16)

    arts_paintingstyle_17 = PaintingStyle()
    arts_paintingstyle_17.name = 'photorealism'
    arts_paintingstyle_17.slug = 'photorealism'
    arts_paintingstyle_17.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_paintingstyle_17.period = None
    arts_paintingstyle_17.location = None
    arts_paintingstyle_17.article =  importer.locate_object(Article, "id", Article, "id", 99, {'id': 99, 'excerpt': 'photorealism', 'kicker': 'photorealism', 'content': '<p>The photorealism art movement started in the late 1960s and became popular in the early 1970s. It is an art genre that strives to create an illusion of a photograph. Photorealism is often mistaken for hyperrealism, which is a related genre.</p>\r\n\r\n<p>The photorealism art movement began in the late 1960s and became popular in the early 1970s. It is an art genre that strives to create an illusion of a photograph. Photorealism is often mistaken for hyperrealism, which is a related genre.</p>\r\n\r\n<p>One of the first photorealist artists was Richard Estes. He became well-known for his paintings of urban scenes. Many of his paintings featured reflections in storefront windows.</p>\r\n\r\n<p>One of the first photorealist artists was Richard Estes. He became well-known for his paintings of urban scenes. Many of his paintings featured reflections in storefront windows.</p>\r\n\r\n<p>Other notable photorealist artists include Chuck Close, who is known for his portraits that feature large-scale close-ups of the subject&#39;s face, and Robert Bechtle, who is known for his realistic images of American suburban life.</p>\r\n\r\n<p>Other notable photorealist artists include Chuck Close, who is known for his portraits that feature large-scale close-ups of the subject&#39;s face, and Robert Bechtle, who is known for his realistic images of American suburban life.</p>\r\n\r\n<p>The photorealism art movement has had a significant influence on subsequent artists. Many artists who are not typically classified as photorealists have been inspired by the movement, including David Hockney and Andreas Gursky.</p>\r\n\r\n<p>The photorealism art movement has had a significant influence on subsequent artists. Many artists who are not typically classified as photorealists have been inspired by the movement, including David Hockney and Andreas Gursky.</p>\r\n\r\n<p>Today, photorealism is still popular and is practiced by a number of artists. The movement has also inspired a number of technological advances, including the development of 3D printing.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:51:09+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:51:24.737715+00:00")} ) 
    arts_paintingstyle_17.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_17 = importer.save_or_locate(arts_paintingstyle_17)

    arts_paintingstyle_18 = PaintingStyle()
    arts_paintingstyle_18.name = 'フォトリアリズム'
    arts_paintingstyle_18.slug = 'photorealism-jp'
    arts_paintingstyle_18.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_paintingstyle_18.period = None
    arts_paintingstyle_18.location = None
    arts_paintingstyle_18.article =  importer.locate_object(Article, "id", Article, "id", 100, {'id': 100, 'excerpt': 'フォトリアリズム', 'kicker': 'フォトリアリズム', 'content': '<p>フォトリアリズムArt Movementは、1960年代後半に始まり、1970年代初頭に人気が出ました。写真のような錯覚を作り出すことを目的とした芸術ジャンルです。フォトリアリズムは、関連するジャンルであるハイパーリアリズムとよく間違えられます。</p>\r\n\r\n<p>フォトリアリズムArt Movementは、1960年代後半に始まり、1970年代初頭に人気が出ました。写真のような幻覚を作り出すことを目的とした芸術ジャンルです。フォトリアリズムは、関連するジャンルであるハイパーリアリズムとよく間違えられます。</p>\r\n\r\n<p>最初の写実主義の芸術家の一人はリチャード・エステスであった。彼は都市の風景を描いた絵で有名になった。彼の絵の多くはショーウィンドウの反射を特徴とした。</p>\r\n\r\n<p>最初の写実主義の芸術家の一人はリチャード・エステスであった。彼は都市の風景を描いた絵で有名になった。彼の絵の多くはショーウィンドウの反射を特徴とした。</p>\r\n\r\n<p>その他の著名な写実主義の芸術家には、被写体の顔を大規模にクローズアップした肖像画で知られるチャック・クローズや、アメリカの郊外の生活をリアルに描いた絵で知られるロバート・ベクトルなどがいる。</p>\r\n\r\n<p>その他の著名な写実主義の芸術家には、被写体の顔を大規模にクローズアップした肖像画で知られるチャック・クローズや、アメリカの郊外の生活をリアルに描いた絵で知られるロバート・ベクトルなどがいる。</p>\r\n\r\n<p>フォトリアリズム・Art Movementは、その後の芸術家に大きな影響を与え、デイヴィッド・ホックニーやアンドレアス・グルスキーなど、通常はphotorealistsに分類されない多くの芸術家がこの運動に触発されている。</p>\r\n\r\n<p>フォトリアリズム・Art Movementは、その後の芸術家に大きな影響を与え、デイヴィッド・ホックニーやアンドレアス・グルスキーなど、通常はphotorealistsに分類されない多くの芸術家がこの運動に触発されている。</p>\r\n\r\n<p>今日、フォトリアリズムは依然として人気があり、多くの芸術家によって実践されている。この運動はまた、3D印刷の開発を含む多くの技術的進歩を促した。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:51:51+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:52:04.287661+00:00")} ) 
    arts_paintingstyle_18.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_18 = importer.save_or_locate(arts_paintingstyle_18)

    arts_paintingstyle_19 = PaintingStyle()
    arts_paintingstyle_19.name = 'realism'
    arts_paintingstyle_19.slug = 'realism'
    arts_paintingstyle_19.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_paintingstyle_19.period = None
    arts_paintingstyle_19.location = None
    arts_paintingstyle_19.article =  importer.locate_object(Article, "id", Article, "id", 101, {'id': 101, 'excerpt': 'realism', 'kicker': 'realism', 'content': '<p>The realism of arts is the accurate, detailed, and sometimes photographic representation of objects, people, and scenes in art. Realism has been used to describe a wide range of artworks, including paintings, sculpture, photography, and even cartooning. The realism of arts has been used to describe a wide range of art movements, including the Realist movement, the Ashcan School, Social Realism, Photorealism, and Pop art.</p>\r\n\r\n<p>Almost from its beginnings, realism has been used to describe accurately the appearance of the world. One of the earliest realistic paintings is the Egyptian tomb painting of the deceased preparing for the afterlife, which dates from about 3,300 years ago. Other ancient examples of realism include the Greek vase paintings, which showed figures and objects in accurate detail, and the Roman frescoes, which captured everyday life.</p>\r\n\r\n<p>The Realist movement began in the mid-19th century and was focused on accurately portraying the world as it was, without idealization. The artists of the movement, including Gustave Courbet and Jean-Fran&ccedil;ois Millet, painted scenes of everyday life, often in rural settings, in a stark and unsentimental style. Other Realist artists depicted the harsh realities of life in industrializing cities, such as the German artist Otto Dix, who portrayed the horrors of World War I.</p>\r\n\r\n<p>The Ashcan School was an early 20th-century American art movement that was inspired by the Realist movement. The Ashcan School artists, including Robert Henri and George Bellows, were interested in capturing the everyday life of the American people, often using gritty and unglamorous subjects.</p>\r\n\r\n<p>Social Realism was a mid-20th-century art movement that was inspired by the Ashcan School. Social Realist artists, including Diego Rivera and Jacob Lawrence, sought to create art that would be useful to the people, often portraying the struggles of the working class.</p>\r\n\r\n<p>Photorealism was a late 20th-century art movement that was inspired by realism. Photorealist artists, including Chuck Close and Richard Estes, sought to create paintings that looked like photographs.</p>\r\n\r\n<p>Pop art was a mid-20th-century art movement that was inspired by realism. Pop artists, including Andy Warhol and Roy Lichtenstein, sought to create art that was based on everyday objects and popular culture.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:52:40+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:53:05.902820+00:00")} ) 
    arts_paintingstyle_19.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_19 = importer.save_or_locate(arts_paintingstyle_19)

    arts_paintingstyle_20 = PaintingStyle()
    arts_paintingstyle_20.name = '写実主義'
    arts_paintingstyle_20.slug = 'realism-jp'
    arts_paintingstyle_20.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_paintingstyle_20.period = None
    arts_paintingstyle_20.location = None
    arts_paintingstyle_20.article =  importer.locate_object(Article, "id", Article, "id", 102, {'id': 102, 'excerpt': 'リアリズム', 'kicker': 'リアリズム', 'content': '<p>芸術のリアリズムとは、芸術における物、人、場面の正確で詳細な、時には写真による表現である。リアリズムは、絵画、彫刻、写真、さらには漫画を含む広範な芸術作品を記述するために使用されてきた。芸術のリアリズムは、リアリスト運動、アシュカン派、社会的リアリズム、フォトリアリズム、ポップアートを含む広範な芸術運動を記述するために使用されてきた。</p>\r\n\r\n<p>リアリズムは、そのほとんどの始まりから、世界の外観を正確に記述するために使用されてきました。最も初期のリアリズム絵画の1つは、約3,300年前のエジプトの死後の世界に備えた死者の墓の絵です。その他の古代のリアリズムの例としては、図形や物体を正確に詳細に示したギリシャの花瓶の絵や、日常生活を捉えたローマのフレスコ画などがあります。</p>\r\n\r\n<p>19世紀半ばに始まったリアリスト運動は、理想化することなく、世界をありのままに正確に描写することに焦点が当てられていた。ギュスターヴ・クールベやジャン=フランソワ・ミレーを含むこの運動の芸術家たちは、日常生活の場面を、しばしば田舎の環境で、辛辣で感傷的でないスタイルで描いた。第一次世界大戦の恐怖を描いたドイツの芸術家オットー・ディクスのような他のリアリスト芸術家たちは、工業化する都市での生活の厳しい現実を描いた。</p>\r\n\r\n<p>アシュカン・スクールは、リアリスト運動に触発された20世紀初頭のアメリカのArt Movementであり、ロバート・ヘンライやジョージ・ベローズを含むアシュカン・スクールの芸術家たちは、アメリカ人の日常生活を捉えることに関心を持ち、しばしば粗野で地味な題材を用いていた。</p>\r\n\r\n<p>ソーシャル・リアリズムは、20世紀半ばのArt Movementで、アシュカン派に触発された。ディエゴ・リベラやジェイコブ・ローレンスを含むソーシャル・リアリズムの芸術家たちは、人々に役立つ芸術を創造しようとし、しばしば労働者階級の闘争を描いた。</p>\r\n\r\n<p>フォトリアリズムは、リアリズムに触発された20世紀後半のArt Movementであり、チャック・クローズやリチャード・エステスを含むフォトリアリズムの芸術家たちは、写真のように見える絵画を作ろうとした。</p>\r\n\r\n<p>ポップアートは、リアリズムに触発された20世紀半ばのArt Movementであり、アンディー・ウォーホールやロイ・リキテンスタインを含むポップ・アーティストは、日常の物や大衆文化に基づいた芸術を創造しようとした。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:53:36+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:53:50.455472+00:00")} ) 
    arts_paintingstyle_20.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_20 = importer.save_or_locate(arts_paintingstyle_20)

    arts_paintingstyle_21 = PaintingStyle()
    arts_paintingstyle_21.name = 'surrealism'
    arts_paintingstyle_21.slug = 'surrealism'
    arts_paintingstyle_21.language =  importer.locate_object(Language, "id", Language, "id", 1, {'id': 1, 'name': 'en'} ) 
    arts_paintingstyle_21.period = None
    arts_paintingstyle_21.location = None
    arts_paintingstyle_21.article =  importer.locate_object(Article, "id", Article, "id", 103, {'id': 103, 'excerpt': 'Surrealism', 'kicker': 'Surrealism', 'content': '<p>Surrealism is a creative movement, started in the early 1920s, that aimed to overthrow rational thinking and to liberate the unconscious mind. The surrealists wanted to create art that expressed the full range of human emotions and desires, not just the ones that fit within the bounds of rational thinking. They believed that the subconscious mind was a far richer source of creativity and inspiration than the conscious mind.</p>\r\n\r\n<p>One of the most famous surrealist artists was Salvador Dali. He was known for his bizarre and fantastical paintings, which often featured melting clocks, elephants wearing watches, and other surreal images. Dali believed that the purpose of art was to astonish and shock the viewer, to make them see the world in a new way.</p>\r\n\r\n<p>Other famous surrealist artists include Jean Arp, Max Ernst, and Yves Tanguy. The surrealist movement had a significant influence on later art movements, including pop art and abstract expressionism.</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:54:21+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:54:37.700135+00:00")} ) 
    arts_paintingstyle_21.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_21 = importer.save_or_locate(arts_paintingstyle_21)

    arts_paintingstyle_22 = PaintingStyle()
    arts_paintingstyle_22.name = 'シュールレアリスム'
    arts_paintingstyle_22.slug = 'surrealism-jp'
    arts_paintingstyle_22.language =  importer.locate_object(Language, "id", Language, "id", 2, {'id': 2, 'name': 'jp'} ) 
    arts_paintingstyle_22.period = None
    arts_paintingstyle_22.location = None
    arts_paintingstyle_22.article =  importer.locate_object(Article, "id", Article, "id", 104, {'id': 104, 'excerpt': 'シュールレアリスム', 'kicker': 'シュールレアリスム', 'content': '<p>シュールレアリスムは、1920年代初頭に始まった創造的な運動で、合理的な思考を覆し、無意識の心を解放することを目的としていました。シュールレアリスムは、合理的な思考の範囲内に収まるものだけでなく、人間の感情や欲望の全範囲を表現する芸術を作りたいと考えていました。彼らは、潜在意識は意識よりもはるかに豊かな創造性とインスピレーションの源であると信じていました。</p>\r\n\r\n<p>最も有名なシュールレアリスムの芸術家の一人はサルバドール・ダリでした。彼は奇妙で幻想的な絵で知られており、しばしば溶ける時計や時計を身につけた象などのシュールなイメージを描いていました。ダリは、芸術の目的は鑑賞者を驚かせ、ショックを与え、彼らに世界を新しい方法で見るようにさせることであると信じていた。</p>\r\n\r\n<p>その他の有名なシュールレアリスム・アーティストには、ジャン・アルプ、マックス・エルンスト、イヴ・タンギーなどがいる。シュールレアリスム運動は、ポップアートや抽象表現主義など、その後の芸術運動に大きな影響を与えた。</p>', 'references': '', 'rating': 0.0, 'rating_count': None, 'published_date': dateutil.parser.parse("2023-06-30T07:55:00+00:00"), 'updated_date': dateutil.parser.parse("2023-06-30T07:55:12.779179+00:00")} ) 
    arts_paintingstyle_22.genre_for_url =  importer.locate_object(GenreForURL, "id", GenreForURL, "id", 5, {'id': 5, 'name': 'arts/painting-styles'} ) 
    arts_paintingstyle_22 = importer.save_or_locate(arts_paintingstyle_22)

    # Re-processing model: arts.models.PaintingStyle























