
import telebot
from random import randint


bot = telebot.TeleBot('token')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    
    if str(message.text).lower() == "/start":
        bot.send_message(
            message.from_user.id, "Привет! Выбери категорию :\n Задачи - /exercises \n Теория - /theory")
    elif str(message.text).lower() == "/theory":
        bot.send_message(
            message.from_user.id, "Выбери тему, задачи по которой ты хочешь посмотреть! \n Кинематика - /kinematictheory \n Динамика - /dynamicstheory \n Закон сохранения импульса /lawsofconservationofthepulsetheory \n Работа и энергия - /workandenergytheory \n Статика - /statictheory \n Гидростатика - /hydrostaticstheory \n Малекулярная физика и газовые законы - /malecularphysicandgaslawstheory \n Термодинамика - /thermodynamicstheory \n Электростатика - /electrostaticstheory \n Справочные материалы - /references")
    elif str(message.text).lower() == "/kinematictheory":
        photo = open("photos\kinematic.png", 'rb')
        bot.send_photo(message.from_user.id, photo)
    elif str(message.text).lower() == "/dynamicstheory":
        photo = open("photos\dynamics.png", 'rb')
        bot.send_photo(message.from_user.id, photo)
    elif str(message.text).lower() == "/lawsofconservationofthepulsetheory":
        photo = open("photos\impulse.png", 'rb')
        bot.send_photo(message.from_user.id, photo)
    elif str(message.text).lower() == "/workandenergytheory":
        photo = open("photos\energyworkn.png", 'rb')
        bot.send_photo(message.from_user.id, photo)
    elif str(message.text).lower() == "/statictheory":
        photo = open("photos\statics.png", 'rb')
        bot.send_photo(message.from_user.id, photo)
    elif str(message.text).lower() == "/hydrostaticstheory":
        photo = open("photos\hydrostatics.png", 'rb')
        bot.send_photo(message.from_user.id, photo)
    elif str(message.text).lower() == "/malecularphysicandgaslawstheory":
        photo = open("photos\malecular1.png", 'rb')
        bot.send_photo(message.from_user.id, photo)
        photo1 = open("photos\malecular2.png", 'rb')
        bot.send_photo(message.from_user.id, photo1)
    elif str(message.text).lower() == "/thermodynamicstheory":
        photo = open("photos\hermodynamics.png", 'rb')
        bot.send_photo(message.from_user.id, photo)
    elif str(message.text).lower() == "/electrostaticstheory":
        photo = open("photos\electrostatics1.png", 'rb')
        bot.send_photo(message.from_user.id, photo)
        photo1 = open("photos\electrostatics2.png", 'rb')
        bot.send_photo(message.from_user.id, photo1)
        photo2 = open("photos\electro3.png", 'rb')
        bot.send_photo(message.from_user.id, photo2)
        photo3 = open("photos\electro4.png", 'rb')
        bot.send_photo(message.from_user.id, photo3)
        photo4 = open("photos\electro5.png", 'rb')
        bot.send_photo(message.from_user.id, photo4)
    elif str(message.text).lower() == "/references":
        photo = open("photos\const.png", 'rb')
        bot.send_photo(message.from_user.id, photo)
        photo = open("photos\s.png", 'rb')
        bot.send_photo(message.from_user.id, photo)





    elif str(message.text).lower() == "/exercises":
        bot.send_message(
            message.from_user.id, "Выбери тему, задачи по которой ты хочешь посмотреть! \n Кинематика - /kinematicexcercises \n Динамика - /dynamics \n Закон сохранения импульса /lawsofconservationofthepulse \n Работа и энергия - /workandenergy \n Статика - /static \n Гидростатика - /hydrostatics \n Малекулярная физика и газовые законы - /malecularphysicandgaslaws \n Термодинамика - /thermodynamics \n Электростатика - /electrostatics \n Постоянный ток - /directcurrent")
    elif str(message.text).lower() == "дай порнуху уебан с мариночкой катагавочкой >;<":
        photo = open("photos\yyKn14IoobA.jpg", 'rb')
        bot.send_photo(message.from_user.id, photo)
    elif str(message.text).lower() == "/kinematicexcercises":
        bot.send_message(
            message.from_user.id, f"1. Пешеход переходил дорогу со скоростью {randint(1,10)} км/ч по прямой, состав-ляющей угол {randint(1,40)}° с направлением дороги, в течение одной минуты. Определите ширину дороги")
        bot.send_message(
            message.from_user.id,f"2. Автомобиль, двигаясь со скоростью {randint(1,10)} км/ч, в течение {randint(1,20)} с прошел такой же путь, какой автобус, двигающийся в том же направлении с постоянной скоростью, прошел за {randint(1,20)} с. Найдите величину их относительной скорости (в км/ч).")
        bot.send_message(
            message.from_user.id,f"3. Велосипедист, проехав {randint(1,10)} км со скоростью {randint(1,20)} км/, остановился и отдыхал в течение {randint(1,50)} мин. Оставшиеся {randint(1,20)} км пути он проехал со скоростью {randint(1,20)} км. Найдите среднюю скорость (в км/ч) велосипедиста на всем пути")
        bot.send_message(
            message.from_user.id,f"4. Тело брошено вертикально вверх с поверхности земли со скоростью {randint(1,80)} м. На какую максимальную высоту оно поднимется? .")
        bot.send_message(
            message.from_user.id,f"5. С неподвижно зависшего над поверхностью земли вертолета сбросилибез начальной скорости два груза, причем второй на {randint(1,10)} с позже пераого. Определите расстояние между грузами через {randint(1,10)} с после начала движения первого груза.9 = 10 м/с")
        bot.send_message(
            message.from_user.id,f"6. Камень, брошенный горизонтально со скоростью {randint(1,30)} м/с, упал на землю со скоростью {randint(1,40)} м/с. Сколько времени длился полет камня? .")
        bot.send_message(
            message.from_user.id,f"7. Камень, брошенный под углом к горизонту, достиг наибольшей высо-ты {randint(1,40)} м. Найдите время полета камня.")    
    elif str(message.text).lower() == "/dynamics":
        bot.send_message(
            message.from_user.id, f"1. Автомобиль массой {randint(1,5)} т, двигавшийся со скоростью {randint(1,72)} км/ч, остановил-ся, пройдя после начала торможения путь {randint(1,30)} м. Определите величину тормозя-щей силы (в кН).")
        bot.send_message(
            message.from_user.id,f"2. Лежащее на горизонтальной поверхности тело приходит в движение под действием горизонтальной силы, составляющей половину действующей на него силы тяжести. Сила действует некоторое время t, потом прекращает действовать. Найдите это время, если известно, что полный путь, пройденный телом до остановки, составляет {randint(1,20)} м, а коэффициент трения 0,2. g = 10 м/с2.")
        bot.send_message(
            message.from_user.id,f"3. Тяжелое тело находится на вершине наклонной плоскости, длина основания и высота которой равны 6 м. Зо сколько секунд тело соскользнет к основанию плоскости, если предельный наклон, при котором тело находится на этой плоскости в покое, имеет место при высоте плоскости {randint(1,20)} м и прежней длине основания {randint(1,20)} м? g = 10 м/с2")
        bot.send_message(
            message.from_user.id,f"4. Два тела, массы которых 0,{randint(1,10)} кг и 0,{randint(1,10)} кг, связаны нитью и лежат на гладкой горизонтальной поверхности. С какой максимальной силой, направленной горизонтально, нужно тянуть первое тело, чтобы нить, способная выдержать нагрузку {randint(1,30)} Н, не оборвалась?")
        bot.send_message(
            message.from_user.id,f"5. Во сколько раз уменьшится сила тяготения между двумя одинаковыми однородными шарами, если вначале шары соприкасались друг с другом, а затем один из шаров отодвинули на расстояние, равное диаметру шаров?")
        bot.send_message(
            message.from_user.id,f"6.  В кабине, укрепленной на конце штанги, находится человек. Штанга с кабиной вращается в вертикальной плоскости с угловой скоростью 0,{randint(1,10)} рад/с. Какова должна быть длина штанги, чтобы человек в верхней точке траектории испытывал состояние невесомости? g = 9,8 м/с2. .")
        bot.send_message(
            message.from_user.id,f"7.На внутренней поверхности сферы радиусом {randint(1,30)} см находится маленькая шайба. До какой минимальной угловой скорости нужно раскрутить сферу вокруг вертикальной оси, чтобы шайба не проскальзывала, находясь на {randint(1,30)} см ниже ее центра? Коэффициент трения 0,5, g = 9,8 м/с2.")
    elif str(message.text).lower() == "/lawsofconservationofthepulse":
        bot.send_message(
            message.from_user.id, f"1. Два одинаковых шарнка массами 3 кг движутся во взаимно перпендику- лярных направлениях со скоростями {randint(1,10)} м/с и {randint(1,10)} м/с. Чему равна величина полного импульса этой системы?.")
        bot.send_message(
            message.from_user.id,f"2. Молот массой {randint(1,10)}000 кг падает с высоты 1,{randint(1,30)} м на наковальню. Длитель- ность удара 0,1 с. Удар неупругий. Определите среднее значение силы взаимо- действия (в кН) молота и наковальни. g = 10 м/с2.")
        bot.send_message(
            message.from_user.id,f"3.  Тележка массой {randint(1,1000)} кг вместе с человеком массой 80 кг движется со скоростью 0,{randint(1,10)} м/с. Человек начинает идти по тележке с постоянной скоростью в направления движения тележки. При какой скоростн (в см/с) человека относительно тележки она остановится?")
        bot.send_message(
            message.from_user.id,f"4.  На вагонетку массой {randint(1,10)}00 кг, катящуюся по горизонтальному пути со скоростью 0,{randint(1,10)} м/с, насыпали сверху {randint(1,10)}00 кг щебня. На сколько при этом уменьшилась скорость (в см/с) вагонетки?")
        bot.send_message(
            message.from_user.id,f"5. Человек захотел спуститься по веревочной лестнице из свободно висящего аэростата массой {randint(1,10)}00 кг. Какой минимальной длины веревочную лестницу он должен привязать к гондоле аэростата, чтобы, ступая на последнюю ступеньку, он коснулся земли? Масса человека 80 кг. Расстояние от земли до аэростата в начальный момент времени {randint(1,10)}0 м.")
        bot.send_message(
            message.from_user.id,f"6. Струя воды ударяется о вертикальную стену, расположенную перпен- дикулярно к струе. После удара вода стекает вниз по стене. Найдите силу, с которой струя действует на стену, если площадь сечения струи {randint(1,10)} см2, а ее скорость {randint(1,20)} м/с.")
    elif str(message.text).lower() == "/workandenergy":
        bot.send_message(
            message.from_user.id, f"1. Груз начинают поднимать вертикально вверх с постоянным ускорением. Во сколько раз работа, совершенная за первую секунду движения, меньше работы, совершаемой за следующую, вторую секунду,")
        bot.send_message(
            message.from_user.id,f"2.  При движении со скоростью {randint(1,100)} км/ч электровоз потребляет мощность {randint(1,10)}0 кВт. Определите силу тяги электровоза, если его КПД равен {randint(1,10)}0%.")
        bot.send_message(
            message.from_user.id,f"3.   Найдите среднюю мощность, которую развивает сила тяжести за первую секунду свободного падения тела массой {randint(1,10)} кг без начальной скорости. g = 10 м/с2.")
        bot.send_message(
            message.from_user.id,f"4.   Камень массой {randint(1,10)}00 г брошен с горизонтальной поверхности под углом к горизонту и упал на нее на расстоянии {randint(1,10)}0 м через {randint(1,10)} с. Чему равна работа, затраченная на этот бросок? g = 10 м/с2")
        bot.send_message(
            message.from_user.id,f"5. Тело массой {randint(1,10)} кг брошено с поверхности земли со скоростью {randint(1,10)} м/с под углом {randint(1,6)}0° к горизонту. На сколько увеличится потенциальная энергия тела при достижении им наивысшей точки подъема?")
        bot.send_message(
            message.from_user.id,f"6. С какой высоты падает без начальной скорости камень, если его скорость при падении на землю {randint(1,20)} м/с, а работа по преодолению силы сопротивления воздуха равна {randint(1,100)}  Дж? Масса камня  {randint(1,10)} кг. g = 10 м/с2.")
    elif str(message.text).lower() == "/static":
        bot.send_message(
            message.from_user.id, f"1. к двум сцепленным динамометрам подвешен груз весом {randint(1,10)} Н. Вес каждого динамометра {randint(1,10)} Н. Сколько покажет верхний динамометр?")
        bot.send_message(
            message.from_user.id,f"2. Стержень длиной 0,{randint(1,10)} м и шар радиусом 0,{randint(1,10)} м соединены вместе, причем ось стержня и центр шара лежат на одной прямой. На каком расстоянии (в см) от середины стержня находится центр тяжести системы, если массы стержня и шара одинаковы?")
        bot.send_message(
            message.from_user.id,f"3. На однородной доске длиной {randint(1,10)} м и массой {randint(1,10)}0 кг качаются два мальчика массами {randint(1,10)}0 и {randint(1,10)}0 кг. На каком расстоянии (в см) от середины должна находиться точка опоры доски, если мальчики сидят на ее концах?")
        bot.send_message(
            message.from_user.id,f"4. Труба весом {randint(1,30)} Н лежит на земле. Какую силу надо приложить, чтобы приподнять трубу за один конец?")
        bot.send_message(
            message.from_user.id,f"5. В однородном шаре радиусом {randint(1,50)} см имеется шарообразная полость вдвое меньшего радиуса, касающаяся поверхности шара. На каком расстоянии (в см) от центра большого шара находится центр тяжести системы?")
        bot.send_message(
            message.from_user.id,f"6. Шар массой {randint(1,10)} кг находится на наклонной плоскости, образующей с горизонтом угол {randint(6,8)}0°. Равновесие шара достигается за счет трения о плоскость и натяжения нити, прикрепленной одним концом к верхней части шара, а другим к вершине наклонной плоскости. Найдите силу натяжения нити, если она располагается горизонтально. g= 10 м/с2. √3=1,7.") 
    elif str(message.text).lower() == "/hydrostatics":
        a={randint(1,10)}
        bot.send_message(
            message.from_user.id, f"1. Высота столба ртути в ртутном барометре {randint(1,100)} см. Какой высоты (в см) столб воды создает такое же давление? Плотность ртути 13600 кг/м3.")
        bot.send_message(
            message.from_user.id,f"2. В сообщающиеся сосуды одинакового сечения налита вода. В один из сосудов поверх воды долили столб масла высотой {randint(1,100)} см. На сколько сантиметров изменится уровень воды в другом сосуде? Плотность масла 800 кг/м3.")
        bot.send_message(
            message.from_user.id,f"3. Тело, имеющее массу {randint(1,10)} кг и объем 0,001 м3, находится в озере на глубине {a} м. Какую работу надо совершить, чтобы медленно поднять его на высоту {randint(1,10)} м над поверхностью воды? g = 10 м/с2.")
        bot.send_message(
            message.from_user.id,f"4. Определите массу (в т) льдины, плавающей в воде, если объем выступающей части льдины {randint(1,10)} м3. Плотность льда 900 кг/м3.")
        bot.send_message(
            message.from_user.id,f"5. Однородный шар массой {randint(1,10)} кг лежит на дне сосуда с водой, который поднимается вертикально вверх с ускорением {randint(1,10)} м/с2. С какой силой давит он на дно сосуда? Плотность материала шарика 4000 кг/м3. g = 10 м/с2.")
        bot.send_message(
            message.from_user.id,f"6. В глубоком цилиндрическом сосуде с водой площадью {randint(1,10)}00 см2 плавает в вертикальном положении цилиндр высотой {randint(1,10)}0см и площадью основания {randint(1,10)}00 см2, сделанный из материала плотностью 500 кг/м3. Какую работу (в мДж) надо совершить, чтобы полностью погрузить цилиндр в воду, если вначале по- верхность воды была на {randint(1,10)} см ниже верхнего края сосуда? g = 10 м/с2.")   
    elif str(message.text).lower() == "/malecularphysicandgaslaws":
        a={randint(1,10)}
        bot.send_message(
            message.from_user.id, f"1. Во сколько раз в {randint(1,5)} г водорода больше молекул, чем в {randint(5,10)} г воды? Моляр- ная масса водорода 2 кг/кмоль, воды 18 кг/кмоль.")
        bot.send_message(
            message.from_user.id,f"2. В объеме 0,00{randint(1,10)} м3 находится газ, масса которого 0,0{randint(1,10)}{randint(1,10)} кг и температура {randint(150,200)}°С. При какой температуре (в кельвинах) плотность этого газа будет 6 кг/м3, если давление останется неизменным?")
        bot.send_message(
            message.from_user.id,f"3. Воздух в открытом сосуде медленно нагрели до {randint(6,10)}00 К, затем сосуд герметично закрыли и охладили до {randint(1,5)}00 К. На сколько процентов при этом изменилось давление в сосуде?")
        bot.send_message(
            message.from_user.id,f"4. Объем цилиндра поршневого насоса равен объему откачиваемого сосуда. Чему будет равно давление в сосуде после 5 ходов поршня насоса? Начальное давление в сосуде равнялось 1{randint(1,10)}{randint(1,10)} Па. Температура постоянна.")
        bot.send_message(
            message.from_user.id,f"5. Газ в количестве 0,0{randint(1,10)} кг при давлении {randint(1,10)}0° Па и температуре {randint(1,10)}{randint(1,10)}°С занимает объем 1660 см3. Определите по этим данным молярную массу (в кг/кмоль) газа. Универсальная газовая постоянная 8300 Дж/(кмоль-К).")
        bot.send_message(
            message.from_user.id,f"6.  На сколько грамм уменьшится масса воздуха в открытом сосуде, если его нагреть от 0°С до 100°C? Начальная масса воздуха {randint(100,500)} г.")
    elif str(message.text).lower() == "/thermodynamics":

        bot.send_message(
            message.from_user.id, f"1. На электроплитке мощностью {randint(1,10)}00 Вт {randint(1,10)} л воды нагреваются до кипения за {randint(1,10)}0 минут. Начальная температура воды {randint(1,10)}{randint(1,10)}°С. Удельная теплоемкость воды 4200 Дж/(кг·К). Определите КПД (в процентах) установки.")
        bot.send_message(
            message.from_user.id,f"2. Какое количество теплоты (в кДж) нужно сообщить {randint(1,10)} кг воды, взятой при {randint(1,50)}°С, чтобы нагреть ее до 100°C и полностью испарить? Удельная теплоемкость воды 4200 Дж/(кг), удельная теплота парообразования воды 2,3-10 Дж/кг.")
        bot.send_message(
            message.from_user.id,f"3. Молот массой {randint(1,10)}000 кг падает с высоты {randint(1,10)} м на металлическую болванку массой {randint(1,10)} кг. В результате удара температура болванки возрастает на {randint(1,10)}{randint(1,10)}°С. Считая, что на нагревание болванки идет 50% всей выделившейся энергии, найдите удельную теплоемкость материала болванки, g = 10 м/с2.")
        bot.send_message(
            message.from_user.id,f"4. Горячее тело при {randint(6,10)}0°C приведено в соприкосновение с холодным телом при {randint(1,5)}0°С. При достижении теплового равновесия установилась температура 50°С. Во сколько раз теплоемкость холодного тела больше теплоемкости горячего?")
        bot.send_message(
            message.from_user.id,f"5. Какую работу совершают два моля некоторого газа при изобарном повышении температуры на {randint(1,10)}0 К? Универсальная газовая постоянная 8300 Дж/(кмоль-К).")
        bot.send_message(
            message.from_user.id,f"6. При изобарном расширении газ совершил работу {randint(1,10)}00 Дж, а его внутренняя энергия увеличилась при этом на {randint(1,10)}{randint(1,10)}0 Дж. Затем газу в изохорном процессе сообщили такое же количество теплоты, как и в первом процессе. На сколько увеличилась внутренняя энергия газа в результате этих двух процессов?") 
        bot.send_message(
            message.from_user.id,f"7. Какое количество теплоты надо сообщить при постоянном давлении {randint(1,10)} моль идеального одноатомного газа, чтобы увеличить его температуру на {randint(1,10)} к? Универсальная газовая постоянная 8300 Дж/(кмоль-К).")
        bot.send_message(
            message.from_user.id,f"8. Идеальная тепловая машина передает холодильнику 80% теплоты, полученной от нагревателя. Найдите температуру (в кельвинах) нагревателя, если температура холодильника  {randint(100,500)} К.")   
    elif str(message.text).lower() == "/electrostatics":
        bot.send_message(
            message.from_user.id, f"1. Два одинаковых маленьких шарика массой {randint(1,10)}0 г каждый подвешены к одной точке на нитях длиной {randint(1,10)}0 см. Какой заряд (в мкКл) надо сообщить каждому шарику, чтобы нити разошлись под прямым углом друг к другу? k = 9*10^9 м/Ф, g = 10 м/с2.")
        bot.send_message(
            message.from_user.id,f"2. Шарик массой {randint(1,10)},{randint(1,10)} г с зарядом 0,{randint(1,10)} мкКл помещен в масло плотностью 800 кг/м3. Плотность материала шарика 1500 кг/м3. Определите напряженность электрического поля (кв/м), в которое следует поместить шарик, чтобы он находился в равновесии. g = 10 м/с2.")
        bot.send_message(
            message.from_user.id,f"3. Напряженность поля, создаваемого небольшим зарядом на расстоянии {randint(1,10)}0 см от него, равна {randint(1,10)}00 В/м. Найдите напряженность поля в точке на расстоянии {randint(1,10)}0 см от заряда.")
        bot.send_message(
            message.from_user.id,f"4. Напряженность электрического поля в плоском конденсаторе {randint(1,10)} 0 кВ/м. Разность потенциалов между обкладками {randint(1,10)} 00 В. Каково расстояние (в мм) между обкладками конденсатора?")
        bot.send_message(
            message.from_user.id,f"5. Какая работа совершается при переносе заряда {randint(1,10)} мкКл из точки поля с потенциалом {randint(1,10)}0 В в другую точку с потенциалом {randint(1,10)}{randint(1,10)} В? В ответе укажите абсолютную величину работы в мкДж.")
        bot.send_message(
            message.from_user.id,f"6. В одной вершине равностороннего треугольника со стороной {randint(1,10)} см зак реплен точечный заряд {randint(1,10)}0 нКл, а в двух других находятся частицы массой {randint(1,10)} мг и зарядом {randint(1,10)}0 нКл каждая. Частицы отпускают, и они приходят в движение. Чему будет равна их скорость на большом расстоянии от заряда? k = 9*10^9 м/Ф.")
        bot.send_message(
            message.from_user.id,f"6. Плоский воздушный конденсатор емкостью {randint(1,10)} мкФ соединили с источником напряжения, в результате чего он приобрел заряд {randint(1,10)}0 мкКл. Расстояние между пластинами конденсатора {randint(1,10)} мм. Определите напряженность поля (в кв/м) внутри конденсатора.")
    elif str(message.text).lower() == "/directcurrent":
        bot.send_message(
            message.from_user.id, f"1. Какой заряд проходит через поперечное сечение проводника в течение {randint(1,10)} с, если за этот промежуток времени сила тока равномерно возрастает от {randint(1,5)} до {randint(6,15)} А?.")
        bot.send_message(
            message.from_user.id,f"2. Вольтметр, рассчитанный на измерение напряжений ло {randint(1,9)} В, необходимо включить в сеть с напряжением {randint(10,20)} В. Какое для этого потребуется дополнительное сопротивление, если сила тока в вольтметре не должна превышать 0,0{randint(1,10)} А?")
        bot.send_message(
            message.from_user.id,f"3. Сколько элементов нужно соединить параллельно в батарею, чтобы при подключении к ней сопротивления {randint(1,10)}{randint(1,10)} Ом получить силу тока в цепи {randint(1,9)} А? ЭДС каждого элемента {randint(1,9)}00 В, внутреннее сопротивление {randint(1,9)} Ом.")
        bot.send_message(
            message.from_user.id,f"4. В цепь последовательно включены вольфрамовая и алюминиевая проволоки одинаковой длины и диаметра. Во сколько раз больше теплоты выделится на вольфрамовой проволоке, если удельное сопротивление вольфрама в два раза больше, чем алюминия?")


    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю ;( . Напиши /start чтобы начать заново")
   








if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
