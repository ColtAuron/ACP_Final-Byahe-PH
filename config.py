import sqlite3
import os
from cryptography.fernet import Fernet

encoding = "utf-8"

# key = b'ZYj4nBF8PylNxTkwv0Py483soXeKz9iIwQdtETXJUro='
# cipher_suit = Fernet(key)
# message = "Hello"
# encoded_text = cipher_suit.encrypt(bytes(message, encoding))
# # print(len(encoded_text))
# decrypt_text = cipher_suit.decrypt(encoded_text)
# # print(decrypt_text.decode())
# print("ZYj4nBF8PylNxTkwv0Py483soXeKz9iIwQdtETXJUro=")
# print(encoded_text)

class Route:
    all = []
    id = 0
    def __init__(self, points, color: str, name: str, disabled=True, ):
        self.points = points
        self.color = color
        self.name = name
        self.disabled = disabled
        Route.all.append(self)

        Route.id += 1
        self.id = Route.id

class Toda:
    all = []
    id = 0
    def __init__(self, position, locName: str, disabled=True ):
        self.position = position
        self.locName = locName
        self.disabled = disabled
        Toda.all.append(self)

        Toda.id += 1
        self.id = Toda.id

class Terminal:
    all = []
    id = 0
    def __init__(self, position, locName: str, disabled=True ):
        self.position = position
        self.locName = locName
        self.disabled = disabled
        Terminal.all.append(self)

        Terminal.id += 1
        self.id = Terminal.id

Bauan = Route(
        [(13.7907420, 121.0101281), # Harap ng Jolibee Bauan
         (13.7922974, 121.0101442), 
         (13.7934297, 121.0100505),
         (13.7934301, 121.0085503),
         (13.7934144, 121.0070805),
         (13.7918202, 121.0072575),
         (13.7901632, 121.0075633),
         (13.7904705, 121.0088561),
         (13.7906236, 121.0095305),
         (13.7906477, 121.0101275),
         (13.7901495, 121.0124423),
         (13.7897848, 121.0141666),
         (13.7891607, 121.0167740),
         (13.7888286, 121.0184105),
         (13.7881760, 121.0203336),
         (13.7842799, 121.0270151),
         (13.7828550, 121.0294656),
         (13.7821054, 121.0314071),
         (13.7811044, 121.0343388),
         (13.7806639, 121.0355507),
         (13.7796428, 121.0379351),
         (13.7782457, 121.0406711),
         (13.7769133, 121.0428646),
         (13.7748676, 121.0457093),
         (13.7735368, 121.0476599),
         (13.7721107, 121.0495955),
         (13.7704713, 121.0515766),
         (13.7694047, 121.0525900),
         (13.7679546, 121.0535725),
         (13.7655470, 121.0550423),
         (13.7634685, 121.0567442),
         (13.7621380, 121.0570915),
         (13.7607421, 121.0573578),
         (13.7583987, 121.0578371),
         (13.7564427, 121.0582627),
         (13.7562376, 121.0565708),
         (13.7538939, 121.0568532),
         (13.7533415, 121.0558972),
         (13.7525904, 121.0552703),     
         (13.7519122, 121.0559817),
         (13.7513291, 121.0565099),
         (13.7506740, 121.0568710),
         (13.7503804, 121.0558426),
         (13.7499046, 121.0550224),
         (13.7497743, 121.0547823),
         (13.7496826, 121.0539033),
         (13.7501929, 121.0535509),
         (13.7507833, 121.0529988),
         (13.7521360, 121.0526551),
         (13.7557086, 121.0519202),
         (13.7569739, 121.0520911),
         (13.7581741, 121.0518183),
         (13.7590183, 121.0517485),
         (13.7613579, 121.0513092),
         (13.7617964, 121.0511526),
         (13.7624008, 121.0520328),
         (13.7628078, 121.0520704),
         (13.7662902, 121.0500083),
         (13.7670075, 121.0488858),
         (13.7673829, 121.0481901),
         (13.7680707, 121.0485227),
         (13.7681738, 121.0486908),
         (13.7685135, 121.0488445),
         (13.7690936, 121.0491575),
         (13.7698387, 121.0497315),
         (13.7711513, 121.0509106),
         (13.7720214, 121.0498109),
         (13.7732637, 121.0482181),
         (13.7757018, 121.0447443),
         (13.7771961, 121.0426750),
         (13.7786774, 121.0400973),
         (13.7802713, 121.0368707),
         (13.7817000, 121.0329887),
         (13.7829865, 121.0294909),
         (13.7882406, 121.0204170),
         (13.7889607, 121.0183341),
         (13.7907420, 121.0101281),
         ],
         color = "Blue",
         name = "Bauan",
         disabled = False,
         )

Capitolio = Route(  #Follow the template and refer sa example sa taas
        [(13.7560889, 121.0707062),  #From SM Batangas Terminal ng Jeep Capitolio
         (13.7574849, 121.0707974), 
         (13.7579033, 121.0708717),
         (13.7581766, 121.0710335), 
         (13.7588039, 121.0717330),
         (13.7590957, 121.0720308),
         (13.7595048, 121.0724770),
         (13.7598591, 121.0728815),
         (13.7602556, 121.0733482),
         (13.7604119, 121.0735145),
         (13.7606776, 121.0737022),
         (13.7615781, 121.0736861),
         (13.7623307, 121.0736459),
         (13.7633467, 121.0735188),
         (13.7637166, 121.0734302),
         (13.7654369,  121.0730547),
         (13.7658111, 121.0729524),
         (13.7669655, 121.0725281),
         (13.7674206, 121.0722959),
         (13.7679655, 121.0718500),
         (13.7683794, 121.0712718),
         (13.7686581, 121.0704376),
         (13.7688012, 121.0698255),
         (13.7689881, 121.0688821),
         (13.7691128, 121.0682415),
         (13.7693993, 121.0669519),
         (13.7694892, 121.0664970),
         (13.7695386, 121.0662567),
         (13.7697028, 121.0655352),
         (13.7697594, 121.0654828),
         (13.7698567, 121.0654922),
         (13.7701016, 121.0655352),
         (13.7706800, 121.0655834),
         (13.7708687, 121.0655761),
         (13.7710099, 121.0654720),
         (13.7708484, 121.0653782),
         (13.7706347, 121.0652628),
         (13.7702143, 121.0650244),
         (13.7696672, 121.0646730),
         (13.7692973, 121.0644391),
         (13.7688487, 121.0641038),
         (13.7680108, 121.0635204),
         (13.7678815, 121.0634668),
         (13.7671012, 121.0627533),
         (13.7667143, 121.0624326),
         (13.7660306, 121.0617502),
         (13.7655770, 121.0611572),
         (13.7651654, 121.0605552),
         (13.7650273, 121.0603082),
         (13.7648716, 121.0601674),
         (13.7647935, 121.0603096),
         (13.7647453, 121.0605242),
         (13.7646021, 121.0612200),
         (13.7645552, 121.0614829),
         (13.7644666, 121.0618287),
         (13.7643685, 121.0623423),
         (13.7642252, 121.0631508),
         (13.7640871, 121.0638643),
         (13.7640458, 121.0640366),
         (13.7640126, 121.0641477),
         (13.7639852, 121.0642777),
         (13.7639370, 121.0644816),
         (13.7639313, 121.0645029),
         (13.7638662, 121.0644787),
         (13.7637711, 121.0644559),
         (13.7635949, 121.0644043),
         (13.7634256, 121.0643386),
         (13.7632518, 121.0642880),
         (13.7629887, 121.0642102),
         (13.7627880, 121.0641465),
         (13.7626290, 121.0640977),
         (13.7621980, 121.0639529),
         (13.7613908, 121.0637111),
         (13.7608619, 121.0635415),
         (13.7606289, 121.0634802),
         (13.7603753, 121.0633826),
         (13.7602031, 121.0633239),
         (13.7600676, 121.0632770),
         (13.7599868, 121.0632462),
         (13.7600025, 121.0631711),
         (13.7600438, 121.0629016),
         (13.7600946, 121.0624125),
         (13.7601454, 121.0619225),
         (13.7602125, 121.0611419),
         (13.7602515, 121.0607442),
         (13.7602524, 121.0606371),
         (13.7601156, 121.0606170),
         (13.7598004, 121.0605741),
         (13.7595846, 121.0605553),
         (13.7594611, 121.0605667),
         (13.7593025, 121.0605768),
         (13.7588570, 121.0606265),
         (13.7587958, 121.0606252),
         (13.7585728, 121.0606413),
         (13.7579198, 121.0606828),
         (13.7577440, 121.0607003),
         (13.7574052, 121.0607324),
         (13.7566421, 121.0607699),
         (13.7564780, 121.0607791),
         (13.7564800, 121.0606923),
         (13.7564836, 121.0604283),
         (13.7564754, 121.0601051),
         (13.7564725, 121.0595369),
         (13.7564530, 121.0590949),
         (13.7564375, 121.0587186),
         (13.7564212, 121.0585247),
         (13.7564114, 121.0584007),
         (13.7564045, 121.0583356),
         (13.7563921, 121.0582345),
         (13.7563953, 121.0581629),
         (13.7563437, 121.0577020),
         (13.7562764, 121.0572315),
         (13.7562332, 121.0568373),
         (13.7561596, 121.0563559),
         (13.7561154, 121.0561085),
         (13.7560928, 121.0559805),
         (13.7562363, 121.0559677),
         (13.7565815, 121.0559623),
         (13.7570236, 121.0559442),
         (13.7573602, 121.0559952),
         (13.7574929, 121.0560418),
         (13.7575074, 121.0560609),
         (13.7576499, 121.0561594),
         (13.7577860, 121.0562607),
         (13.7579675, 121.0563890),
         (13.7581863, 121.0565459),
         (13.7582977, 121.0566388),
         (13.7583601, 121.0566910),
         (13.7586609, 121.0568909),
         (13.7589566, 121.0571659),
         (13.7592001, 121.0575863),
         (13.7592540, 121.0577041),
         (13.7593119, 121.0579038),
         (13.7593594, 121.0581964),
         (13.7593936, 121.0583983),
         (13.7594305, 121.0586638),
         (13.7594509, 121.0588037),
         (13.7594561, 121.0588466),
         (13.7594682, 121.0588499),
         (13.7596297, 121.0588586),
         (13.7598626, 121.0588727),
         (13.7599121, 121.0588780),
         (13.7601391, 121.0589341),
         (13.7604023, 121.0589946),
         (13.7608595, 121.0590509),
         (13.7611122, 121.0590968),
         (13.7615285, 121.0591640),
         (13.7617524, 121.0592035),
         (13.7617832, 121.0592065),
         (13.7617812, 121.0591961),
         (13.7617809, 121.0591391),
         (13.7617809, 121.0589908),
         (13.7617834, 121.0588109),
         (13.7617775, 121.0584493),
         (13.7617705, 121.0579807),
         (13.7617535, 121.0575171),
         (13.7617327, 121.0572066),
         (13.7617325, 121.0571998),
         (13.7618009, 121.0571871),
         (13.7618924, 121.0571706),
         (13.7620129, 121.0571522),
         (13.7621968, 121.0571274),
         (13.7622347, 121.0571201),
         (13.7622494, 121.0571472),
         (13.7623000, 121.0572038),
         (13.7623635, 121.0572549),
         (13.7625419, 121.0573521),
         (13.7629151, 121.0576002),
         (13.7631236, 121.0577524),
         (13.7633885, 121.0579883),
         (13.7636934, 121.0583438),
         (13.7639005, 121.0586336),
         (13.7641945, 121.0590369),
         (13.7645803, 121.0596704),
         (13.7648292, 121.0600915),
         (13.7648544, 121.0601292),
         (13.7648341, 121.0601416),
         (13.7647800, 121.0602167),
         (13.7647253, 121.0603716),
         (13.7646792, 121.0605896),
         (13.7645880, 121.0610451),
         (13.7645046, 121.0614486),
         (13.7643855, 121.0619694),
         (13.7643154, 121.0623171),
         (13.7642620, 121.0626520),
         (13.7641663, 121.0631761),
         (13.7640464, 121.0638297),
         (13.7639591, 121.0641518),
         (13.7639481, 121.0642025),
         (13.7639720, 121.0642534),
         (13.7640299, 121.0643761),
         (13.7641172, 121.0645001),
         (13.7641943, 121.0645778),
         (13.7647205, 121.0646650),
         (13.7652452, 121.0647655),
         (13.7657232, 121.0648511),
         (13.7661192, 121.0649168),
         (13.7661646, 121.0649155),
         (13.7661301, 121.0650070),
         (13.7660382, 121.0654868),
         (13.7659764, 121.0658670),
         (13.7659093, 121.0662727),
         (13.7658619, 121.0665704),
         (13.7658944, 121.0665828),
         (13.7658993, 121.0665700),
         (13.7658762, 121.0665650),
         (13.7658876, 121.0665003),
         (13.7659060, 121.0663799),
         (13.7659570, 121.0660676),
         (13.7660171, 121.0656944),
         (13.7660401, 121.0655548),
         (13.7661099, 121.0651806),
         (13.7661521, 121.0650522),
         (13.7661964, 121.0649274),
         (13.7668680, 121.0650414),
         (13.7693856, 121.0654207),
         (13.7696950, 121.0654447),
         (13.7696480, 121.0655735),
         (13.7693537, 121.0668260),
         (13.7691657, 121.0676361),
         (13.7689339, 121.0687798),
         (13.7685398, 121.0706031),
         (13.7684491, 121.0709005),
         (13.7683019, 121.0712733),
         (13.7681191, 121.0715590),
         (13.7679064, 121.0718153),
         (13.7676536, 121.0720546),
         (13.7672117, 121.0723416),
         (13.7668018, 121.0725410),
         (13.7661209, 121.0727850),
         (13.7649984, 121.0730935),
         (13.7638048, 121.0733421),
         (13.7631553, 121.0734772),
         (13.7624139, 121.0735791),
         (13.7609999, 121.0736408),
         (13.7607190, 121.0736435),
         (13.7606661, 121.0736272),
         (13.7605085, 121.0735172),
         (13.7601868, 121.0731605),
         (13.7596610, 121.0725654),
         (13.7589516, 121.0717833),
         (13.7582842, 121.0710847),
         (13.7581525, 121.0709520),
         (13.7580008, 121.0708528),
         (13.7574176, 121.0707281),
         (13.7569252, 121.0706972),
         (13.7566836, 121.0706945),
         (13.7566744, 121.0705557),
         (13.7566153, 121.0694991),
         (13.7565501, 121.0682368),
         (13.7565232, 121.0674624),
         (13.7563028, 121.0673427),
         (13.7561725, 121.0672072),
         (13.7559311, 121.0670737),
         (13.7557485, 121.0670298),
         (13.7550262, 121.0668271),
         (13.7541744, 121.0666206),
         (13.7537865, 121.0665173),
         (13.7537024, 121.0665093),
         (13.7536904, 121.0667658),
         (13.7536657, 121.0675095),
         (13.7537283, 121.0687366),
         (13.7539836, 121.0700834),
         (13.7540463, 121.0703114),
         (13.7546295, 121.0706038),
         (13.7555571, 121.0707004),
         (13.7556848, 121.0706923),
         (13.7560704, 121.0707051),
         (13.7560900, 121.0707058), #SM Batangas

         ],
         color = "Gray",
         name = "Capitolio",
         disabled = False,   #Set to false para makita nyo sa map TY!
         )

Balagtas = Route(  
        [(13.7906009, 121.0610644),  #Grand Terminal
         (13.7900835, 121.0620799),
         (13.7897686, 121.0619649),
         (13.7895834, 121.0619512),
         (13.7894427, 121.0620858),
         (13.7892469, 121.0624769),
         (13.7889434, 121.0630987),
         (13.7889810, 121.0631969),
         (13.7891280, 121.0632659),
         (13.7893509, 121.0632559),
         (13.7895969, 121.0630763),
         (13.7897740, 121.0627939),
         (13.7901063, 121.0621401),
         (13.7905666, 121.0623675),
         (13.7910815, 121.0614192),
         (13.7943339, 121.0631048),
         (13.7946997, 121.0635419),
         (13.7960802, 121.0643207),
         (13.7965420, 121.0647059),
         (13.7968154, 121.0651253),
         (13.7968760, 121.0653024),
         (13.7970204, 121.0678350),
         (13.7974303, 121.0707608),
         (13.7922138, 121.0701176),
         (13.7891648, 121.0697193),
         (13.7865072, 121.0691032),
         (13.7848040, 121.0686035),
         (13.7838446, 121.0684919),
         (13.7833812, 121.0684158),
         (13.7799199, 121.0676808),
         (13.7780654, 121.0669153),
         (13.7764457, 121.0665064),
         (13.7747160, 121.0662574),
         (13.7725408, 121.0658730),
         (13.7710913, 121.0654842),
         (13.7695725, 121.0646184),
         (13.7678718, 121.0634349),
         (13.7666512, 121.0623770),
         (13.7657994, 121.0615362),
         (13.7649130, 121.0601337),
         (13.7647174, 121.0602532),
         (13.7644743, 121.0614431),
         (13.7638717, 121.0644427),
         (13.7613060, 121.0636511),
         (13.7599974, 121.0632201),
         (13.7602708, 121.0606805),
         (13.7595969, 121.0605462),
         (13.7580765, 121.0606462),
         (13.7565176, 121.0607538),
         (13.7564658, 121.0584234),
         (13.7563279, 121.0572217),
         (13.7541955, 121.0574609),
         (13.7533195, 121.0558790),
         (13.7525630, 121.0552516),
         (13.7513239, 121.0564536),
         (13.7506694, 121.0568179),
         (13.7503841, 121.0558578),
         (13.7499016, 121.0549798),
         (13.7497816, 121.0547867),
         (13.7496826, 121.0538962),
         (13.7502183, 121.0535353),
         (13.7508337, 121.0529525),
         (13.7552196, 121.0520328),
         (13.7557400, 121.0547994),
         (13.7573038, 121.0546647),
         (13.7574709, 121.0560875),
         (13.7585202, 121.0568349),
         (13.7587979, 121.0570367),
         (13.7590464, 121.0573278),
         (13.7592222, 121.0577088),
         (13.7592974, 121.0580303),
         (13.7594201, 121.0588877),
         (13.7598871, 121.0589103),
         (13.7603676, 121.0590111),
         (13.7608619, 121.0590486), 
         (13.7607749, 121.0574302),
         (13.7621806, 121.0571585),
         (13.7633123, 121.0579496),
         (13.7648785, 121.0602297),
         (13.7648072, 121.0603368),
         (13.7644721, 121.0619349),
         (13.7640160, 121.0641886),
         (13.7641677, 121.0644742),
         (13.7664720, 121.0648838),
         (13.7699418, 121.0654367),
         (13.7711417, 121.0655982),
         (13.7715048, 121.0657286),
         (13.7740313, 121.0662554),
         (13.7764355, 121.0666080),
         (13.7784669, 121.0671766),
         (13.7798635, 121.0677924),
         (13.7836540, 121.0685839),
         (13.7848190, 121.0687376),
         (13.7866118, 121.0692349),
         (13.7894819, 121.0699232),
         (13.7922115, 121.0702477),
         (13.7966758, 121.0707291),
         (13.7972333, 121.0712053),
         (13.7975274, 121.0713394),
         (13.7977247, 121.0711583),
         (13.7977062, 121.0709445),
         (13.7975371, 121.0707936),
         (13.7971522, 121.0677890),
         (13.7970117, 121.0652878),
         (13.7966231, 121.0645961),
         (13.7947587, 121.0634605),
         (13.7943815, 121.0630215),
         (13.7906009, 121.0610644),
         ],
         color = "Yellow",
         name = "Balagtas",
         disabled = False,   #Set to false para makita nyo sa map TY!
         )

Alangilan= Route(
        [#Grand Terminal
         (13.7894625, 121.0620557),
         (13.7895771, 121.0619592),
         (13.7896917, 121.0619646),
         (13.7900825, 121.0620906),
         (13.7902932, 121.0616817),
         (13.7905994, 121.0610757),
         (13.7911250, 121.0613493),
         (13.7925048, 121.0620511),
         (13.7943679, 121.0630037),
         (13.7947839, 121.0634928),
         (13.7952111, 121.0637342),
         (13.7962634, 121.0643350),
         (13.7966039, 121.0646674),
         (13.7969947, 121.0652843),
         (13.7970607, 121.0666410),
         (13.7972802, 121.0689955),
         (13.7975086, 121.0707756),
         (13.7977118, 121.0709365),
         (13.7977222, 121.0712691),
         (13.7976046, 121.0713537),
         (13.7972504, 121.0711954),
         (13.7969769, 121.0709218),
         (13.7967017, 121.0707394),
         (13.7966382, 121.0706914),
         (13.7961147, 121.0706404),
         (13.7954883, 121.0705492),
         (13.7936278, 121.0703352),
         (13.7922055, 121.0702065),
         (13.7910097, 121.0700968),
         (13.7899938, 121.0699842),
         (13.7893003, 121.0698460),
         (13.7875821, 121.0694597),
         (13.7865852, 121.0692158),
         (13.7848224, 121.0687355),
         (13.7843191, 121.0686470),
         (13.7836741, 121.0685487),
         (13.7830317, 121.0684255),
         (13.7811594, 121.0680403),
         (13.7800461, 121.0678069),
         (13.7797196, 121.0677023),
         (13.7794565, 121.0675897),
         (13.7789433, 121.0673429),
         (13.7785201, 121.0671650),
         (13.7779965, 121.0669895),
         (13.7764413, 121.0666048),
         (13.7754027, 121.0664224),
         (13.7743121, 121.0662775),
         (13.7728064, 121.0659891),
         (13.7725205, 121.0659613),
         (13.7709550, 121.0655819),
         (13.7696955, 121.0654907),
         (13.7661550, 121.0649332),
         (13.7640627, 121.0645417),
         (13.7620046, 121.0639388),
         (13.7599683, 121.0632998),
         (13.7591190, 121.0630738),
         (13.7582872, 121.0630309),
         (13.7580478, 121.0607071),
         (13.7578188, 121.0590278),
         (13.7577111, 121.0580781),
         (13.7575704, 121.0570476),
         (13.7574696, 121.0564496),
         (13.7574888, 121.0560807),
         (13.7570511, 121.0559627),
         (13.7561027, 121.0559841),
         (13.7558223, 121.0547962),
         (13.7554159, 121.0527880),
         (13.7552387, 121.0519995),
         (13.7515373, 121.0527524),
         (13.7507861, 121.0529670),
         (13.7496658, 121.0539165),
         (13.7497552, 121.0547650),
         (13.7503723, 121.0558469),
         (13.7506537, 121.0568604),
         (13.7513181, 121.0564729),
         (13.7517673, 121.0560841),
         (13.7525447, 121.0552754),
         (13.7533074, 121.0558961),
         (13.7538754, 121.0568740),
         (13.7541412, 121.0575017),
         (13.7562621, 121.0572311),
         (13.7575687, 121.0570541),
         (13.7582396, 121.0569856),
         (13.7584556, 121.0579004),
         (13.7592595, 121.0577062),
         (13.7622325, 121.0571246),
         (13.7649269, 121.0601667),
         (13.7659177, 121.0617009),
         (13.7678455, 121.0635248),
         (13.7693116, 121.0645041),
         (13.7705985, 121.0652899),
         (13.7712508, 121.0655458),
         (13.7725572, 121.0658721),
         (13.7763003, 121.0664651),
         (13.7776456, 121.0667774),
         (13.7787251, 121.0671346),
         (13.7799877, 121.0677117),
         (13.7823504, 121.0681856),
         (13.7848437, 121.0686339),
         (13.7872639, 121.0692967),
         (13.7901946, 121.0698803),
         (13.7941703, 121.0703201),
         (13.7966133, 121.0706098),
         (13.7971228, 121.0706903),
         (13.7974615, 121.0707868),
         (13.7970707, 121.0678107),
         (13.7968936, 121.0653105),
         (13.7965602, 121.0646957),
         (13.7960497, 121.0642826),
         (13.7952057, 121.0638320),
         (13.7947226, 121.0635224),
         (13.7943182, 121.0630684),
         (13.7941463, 121.0629711),
         (13.7910960, 121.0614208),
         (13.7910597, 121.0614109),
         (13.7905648, 121.0623209),
         (13.7901116, 121.0621198),
         (13.7894728, 121.0631687),
         (13.7893478, 121.0632277),
         (13.7891352, 121.0632454),
         (13.7889659, 121.0631166),
         (13.7894618, 121.0620525),
         ],
         color = "Green",
         name = "Alangilan",
         disabled = False,  
         )

Coliseum_Toda = Toda(
    position = (13.7525742, 121.0520111),
    locName = "Coliseum",
    disabled = False
)

PlazaMabini_Toda = Toda(
    position = (13.7553644, 121.0594922),
    locName = "Plaza Mabini",
    disabled = False
)

RizalAve_Toda = Toda(
    position = (13.7553557, 121.0517192),
    locName = "Rizal Ave.",
    disabled = False
)

Diversion_Toda = Toda(
    position= (13.7716671, 121.0507626),
    locName= "Diversion",
    disabled= False
)

SanAntonio_Toda = Toda(
    position= (13.7880907, 121.0202637),
    locName= "San Antonio",
    disabled= False
)

BauanPubMarket_Toda = Toda(
    position = (13.7925640, 121.0100531),
    locName= "Bauan Public Market",
    disabled= False
)

Goldland_Toda = Toda(
    position= (13.7924336, 121.0109337),
    locName= "Goldland",
    disabled= False
)

Balagtas_Toda = Toda(
    position= (13.7980044, 121.0710054),
    locName= "Balagtas",
    disabled= False
)

GoldenCountry_Toda = Toda(
    position= (13.7865083, 121.0694451),
    locName= "Golden Country",
    disabled= False
)

BatangasPier_Terminal = Terminal(
    position=(13.7536221, 121.0434020),
    locName=("Batangas Pier"),
    disabled= False
)

BatangasGrand_Terminal = Terminal(
    position= (13.7894298, 121.0627731),
    locName=("Batangas Grand"),
    disabled= False
)

# command = ('''CREATE TABLE IF NOT EXISTS ROUTE(
#             RouteNum INTEGER PRIMARY KEY,
#             Name Varchar(30),
#             Color Varchar(20),
#             Disabled TINYINT(1)
#            )''')

# con.execute(command)

# command = ('''CREATE TABLE IF NOT EXISTS POINTS(
#            Id INTEGER PRIMARY KEY,
#            Point_X FLOAT(3, 7),
#            Point_Y FLOAT(3, 7),
#            RouteNum INTEGER,
#            FOREIGN KEY(RouteNum) REFERENCES ROUTE(RouteNum)
# )''')

# con.execute(command)

# command = ('''CREATE TABLE IF NOT EXISTS TODA(
#             TodaID INTEGER PRIMARY KEY,
#             Point_X FLOAT(3, 7),
#             Point_Y FLOAT(3, 7),
#             locName Varchar(100),
#             Disabled TINYINT(1)
#            )''')

# con.execute(command)

# command = ('''CREATE TABLE IF NOT EXISTS TERMINAL(
#             TemiID INTEGER PRIMARY KEY,
#             Point_X FLOAT(3, 7),
#             Point_Y FLOAT(3, 7),
#             locName Varchar(100),
#             Disabled TINYINT(1)
#            )''')

# con.execute(command)

# command = ('''CREATE TABLE IF NOT EXISTS DRAWPOINTS(
#            Id INTEGER PRIMARY KEY,
#            Point_X FLOAT(3, 7),
#            Point_Y FLOAT(3, 7)
# )''')

# con.execute(command)

# c.execute

# tosql = []
# for todas in Toda.all:
#     tosql.append(tuple((todas.id, todas.position[0], todas.position[1], todas.locName, todas.disabled)))

# c.executemany("INSERT INTO TODA VALUES (?,?,?,?,?)", tosql)
# con.commit()

# tosql = []
# for termi in Terminal.all:
#     tosql.append(tuple((termi.id, termi.position[0], termi.position[1], termi.locName, termi.disabled)))

# c.executemany("INSERT INTO TERMINAL VALUES (?,?,?,?,?)", tosql)
# con.commit()

# tosql = []
# for jeepneys in Route.all:
#     tosql.append(tuple((jeepneys.id, jeepneys.name, jeepneys.color, int(jeepneys.disabled))))

# c.executemany("INSERT INTO ROUTE VALUES (?,?,?,?)", tosql)

# con.commit()

# tosql = []

# for jeepneys in Route.all:
#     for points in jeepneys.points:
#         tosql.append(tuple((points[0], points[1], jeepneys.id)))

# c.executemany("INSERT INTO POINTS(Point_X, Point_Y, RouteNum) VALUES (?,?,?)", tosql)

# con.commit()

# c.execute("SELECT * FROM POINTS")
# points_table = c.fetchall()

# c.execute("SELECT * FROM ROUTE")
# route_table = c.fetchall()

# for jeepneys in route_table:
#     if jeepneys[3] == 0:
#         c.execute(f"SELECT Point_X, Point_Y FROM POINTS WHERE RouteNum = {jeepneys[0]}")
#         points = c.fetchall()
#         print(points, color = jeepneys[2], width = 3)

# c.execute("SELECT * FROM TODA")
# toda_table = c.fetchall()
# for toda in toda_table:
#     print(toda)

# c.execute("SELECT * FROM TERMINAL")
# termi_table = c.fetchall()
# for toda in termi_table:
#     print(toda)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "bphData.db")
con = sqlite3.connect(db_path)
c = con.cursor()


command = ('''CREATE TABLE IF NOT EXISTS ACCOUNT(
            ID INTEGER PRIMARY KEY,
            Email Varchar(30),
            User Varchar(20),
            Password Varchar(103),
            Admin TINYINT(1)
           )''')

# command = ('''CREATE TABLE IF NOT EXISTS KEY(
#             KEY Varchar(44)
#            )''')

c.execute(command)

# # # c.execute("SELECT Email FROM ACCOUNT WHERE Email=?", (email,))
# # # # email_table = c.fetchall()

# # c.execute("INSERT INTO KEY VALUES ('ZYj4nBF8PylNxTkwv0Py483soXeKz9iIwQdtETXJUro=')")
# # con.commit()

# command = ('''CREATE TABLE IF NOT EXISTS KEEPSIGNED(
#             ID INTEGER PRIMARY KEY,
#             UserID INTEGER,
#             Password Varchar(103),
#             Keep TINYINT(1)
#            )''')

# c.execute(command)
# c.execute("DELETE FROM KEEPSIGNED")
# con.commit()
# keep_table = c.fetchall()
# print(keep_table)

# c.execute("SELECT * FROM ACCOUNT WHERE ID=?", (keep_table[0][0],))
# key_table = c.fetchall()
# print(key_table)

# keep_table = 1 
# c.execute("SELECT * FROM KEEPSIGNED")
# user_table = c.fetchall()
# print(user_table)

# command = ('''CREATE TABLE IF NOT EXISTS REQUESTROUTE(
#             RouteNum INTEGER PRIMARY KEY,
#             Name Varchar(30),
#             Color Varchar(20),
#             Author Varchar(20)
#            )''')

# con.execute(command)

# command = ('''CREATE TABLE IF NOT EXISTS REQUESTPOINTS(
#            Id INTEGER PRIMARY KEY,
#            Point_X FLOAT(3, 7),
#            Point_Y FLOAT(3, 7),
#            RouteNum INTEGER,
#            FOREIGN KEY(RouteNum) REFERENCES REQUESTROUTE(RouteNum)
# )''')

# c.execute("DELETE FROM KEEPSIGNED")
# con.commit()


# c.execute("UPDATE REQUESTROUTE SET Author = 3 WHERE RouteNum=1")
# con.commit()
# c.execute("DELETE FROM ROUTE WHERE RouteNum=5")
# con.commit()
c.execute("SELECT * FROM TODA")
print(c.fetchall())


con.close()









