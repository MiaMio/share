from EmQuantAPI import *
from datetime import timedelta, datetime
import time
import json

def login():
	loginResult = c.start("ForceLogin=1")
	if(loginResult.ErrorCode != 0):
		print("login in fail")
		exit()
	print("login in successful!")

def addMACD():
	timestamp=time.time()
	today_time=time.strftime("%Y-%m-%d", time.localtime(time.time()))

	date="2018/4/12"
	data=c.css("000001.SZ,000002.SZ,000004.SZ,000005.SZ,000006.SZ,000007.SZ,000008.SZ,000009.SZ,000010.SZ,000011.SZ,000012.SZ,000014.SZ,000016.SZ,000017.SZ,000018.SZ,000019.SZ,000020.SZ,000021.SZ,000022.SZ,000023.SZ,000025.SZ,000026.SZ,000027.SZ,000028.SZ,000029.SZ,000030.SZ,000031.SZ,000032.SZ,000034.SZ,000035.SZ,000036.SZ,000037.SZ,000038.SZ,000039.SZ,000040.SZ,000042.SZ,000043.SZ,000045.SZ,000046.SZ,000048.SZ,000049.SZ,000050.SZ,000055.SZ,000056.SZ,000058.SZ,000059.SZ,000060.SZ,000061.SZ,000062.SZ,000063.SZ,000065.SZ,000066.SZ,000068.SZ,000069.SZ,000070.SZ,000078.SZ,000088.SZ,000089.SZ,000090.SZ,000096.SZ,000099.SZ,000100.SZ,000150.SZ,000151.SZ,000153.SZ,000155.SZ,000156.SZ,000157.SZ,000158.SZ,000159.SZ,000166.SZ,000301.SZ,000333.SZ,000338.SZ,000400.SZ,000401.SZ,000402.SZ,000403.SZ,000404.SZ,000407.SZ,000408.SZ,000409.SZ,000410.SZ,000411.SZ,000413.SZ,000415.SZ,000416.SZ,000417.SZ,000418.SZ,000419.SZ,000420.SZ,000421.SZ,000422.SZ,000423.SZ,000425.SZ,000426.SZ,000428.SZ,000429.SZ,000430.SZ,000488.SZ,000498.SZ,000501.SZ,000502.SZ,000503.SZ,000504.SZ,000505.SZ,000506.SZ,000507.SZ,000509.SZ,000510.SZ,000511.SZ,000513.SZ,000514.SZ,000516.SZ,000517.SZ,000518.SZ,000519.SZ,000520.SZ,000521.SZ,000523.SZ,000524.SZ,000525.SZ,000526.SZ,000528.SZ,000529.SZ,000530.SZ,000531.SZ,000532.SZ,000533.SZ,000534.SZ,000536.SZ,000537.SZ,000538.SZ,000539.SZ,000540.SZ,000541.SZ,000543.SZ,000544.SZ,000545.SZ,000546.SZ,000547.SZ,000548.SZ,000550.SZ,000551.SZ,000552.SZ,000553.SZ,000554.SZ,000555.SZ,000557.SZ,000558.SZ,000559.SZ,000560.SZ,000561.SZ,000563.SZ,000564.SZ,000565.SZ,000566.SZ,000567.SZ,000568.SZ,000570.SZ,000571.SZ,000572.SZ,000573.SZ,000576.SZ,000581.SZ,000582.SZ,000584.SZ,000585.SZ,000586.SZ,000587.SZ,000589.SZ,000590.SZ,000591.SZ,000592.SZ,000593.SZ,000595.SZ,000596.SZ,000597.SZ,000598.SZ,000599.SZ,000600.SZ,000601.SZ,000603.SZ,000605.SZ,000606.SZ,000607.SZ,000608.SZ,000609.SZ,000610.SZ,000611.SZ,000612.SZ,000613.SZ,000615.SZ,000616.SZ,000617.SZ,000619.SZ,000620.SZ,000622.SZ,000623.SZ,000625.SZ,000626.SZ,000627.SZ,000628.SZ,000629.SZ,000630.SZ,000631.SZ,000632.SZ,000633.SZ,000635.SZ,000636.SZ,000637.SZ,000638.SZ,000639.SZ,000650.SZ,000651.SZ,000652.SZ,000655.SZ,000656.SZ,000657.SZ,000659.SZ,000661.SZ,000662.SZ,000663.SZ,000665.SZ,000666.SZ,000667.SZ,000668.SZ,000669.SZ,000670.SZ,000671.SZ,000672.SZ,000673.SZ,000676.SZ,000677.SZ,000678.SZ,000679.SZ,000680.SZ,000681.SZ,000682.SZ,000683.SZ,000685.SZ,000686.SZ,000687.SZ,000688.SZ,000690.SZ,000691.SZ,000692.SZ,000693.SZ,000695.SZ,000697.SZ,000698.SZ,000700.SZ,000701.SZ,000702.SZ,000703.SZ,000705.SZ,000707.SZ,000708.SZ,000709.SZ,000710.SZ,000711.SZ,000712.SZ,000713.SZ,000715.SZ,000716.SZ,000717.SZ,000718.SZ,000719.SZ,000720.SZ,000721.SZ,000722.SZ,000723.SZ,000725.SZ,000726.SZ,000727.SZ,000728.SZ,000729.SZ,000731.SZ,000732.SZ,000733.SZ,000735.SZ,000736.SZ,000737.SZ,000738.SZ,000739.SZ,000750.SZ,000751.SZ,000752.SZ,000753.SZ,000755.SZ,000756.SZ,000757.SZ,000758.SZ,000759.SZ,000760.SZ,000761.SZ,000762.SZ,000766.SZ,000767.SZ,000768.SZ,000776.SZ,000777.SZ,000778.SZ,000779.SZ,000780.SZ,000782.SZ,000783.SZ,000785.SZ,000786.SZ,000788.SZ,000789.SZ,000790.SZ,000791.SZ,000792.SZ,000793.SZ,000795.SZ,000796.SZ,000797.SZ,000798.SZ,000799.SZ,000800.SZ,000801.SZ,000802.SZ,000803.SZ,000806.SZ,000807.SZ,000809.SZ,000810.SZ,000811.SZ,000812.SZ,000813.SZ,000815.SZ,000816.SZ,000818.SZ,000819.SZ,000820.SZ,000821.SZ,000822.SZ,000823.SZ,000825.SZ,000826.SZ,000828.SZ,000829.SZ,000830.SZ,000831.SZ,000833.SZ,000835.SZ,000836.SZ,000837.SZ,000838.SZ,000839.SZ,000848.SZ,000850.SZ,000851.SZ,000852.SZ,000856.SZ,000858.SZ,000859.SZ,000860.SZ,000861.SZ,000862.SZ,000863.SZ,000868.SZ,000869.SZ,000875.SZ,000876.SZ,000877.SZ,000878.SZ,000880.SZ,000881.SZ,000882.SZ,000883.SZ,000885.SZ,000886.SZ,000887.SZ,000888.SZ,000889.SZ,000890.SZ,000892.SZ,000893.SZ,000895.SZ,000897.SZ,000898.SZ,000899.SZ,000900.SZ,000901.SZ,000902.SZ,000903.SZ,000905.SZ,000906.SZ,000908.SZ,000909.SZ,000910.SZ,000911.SZ,000912.SZ,000913.SZ,000915.SZ,000917.SZ,000918.SZ,000919.SZ,000920.SZ,000921.SZ,000922.SZ,000923.SZ,000925.SZ,000926.SZ,000927.SZ,000928.SZ,000929.SZ,000930.SZ,000931.SZ,000932.SZ,000933.SZ,000935.SZ,000936.SZ,000937.SZ,000938.SZ,000939.SZ,000948.SZ,000949.SZ,000950.SZ,000951.SZ,000952.SZ,000953.SZ,000955.SZ,000957.SZ,000958.SZ,000959.SZ,000960.SZ,000961.SZ,000962.SZ,000963.SZ,000965.SZ,000966.SZ,000967.SZ,000968.SZ,000969.SZ,000970.SZ,000971.SZ,000972.SZ,000973.SZ,000975.SZ,000976.SZ,000977.SZ,000978.SZ,000979.SZ,000980.SZ,000981.SZ,000982.SZ,000983.SZ,000985.SZ,000987.SZ,000988.SZ,000989.SZ,000990.SZ,000993.SZ,000995.SZ,000996.SZ,000997.SZ,000998.SZ,000999.SZ,001696.SZ,001896.SZ,001965.SZ,001979.SZ,002001.SZ,002002.SZ,002003.SZ,002004.SZ,002005.SZ,002006.SZ,002007.SZ,002008.SZ,002009.SZ,002010.SZ,002011.SZ,002012.SZ,002013.SZ,002014.SZ,002015.SZ,002016.SZ,002017.SZ,002018.SZ,002019.SZ,002020.SZ,002021.SZ,002022.SZ,002023.SZ,002024.SZ,002025.SZ,002026.SZ,002027.SZ,002028.SZ,002029.SZ,002030.SZ,002031.SZ,002032.SZ,002033.SZ,002034.SZ,002035.SZ,002036.SZ,002037.SZ,002038.SZ,002039.SZ,002040.SZ,002041.SZ,002042.SZ,002043.SZ,002044.SZ,002045.SZ,002046.SZ,002047.SZ,002048.SZ,002049.SZ,002050.SZ,002051.SZ,002052.SZ,002053.SZ,002054.SZ,002055.SZ,002056.SZ,002057.SZ,002058.SZ,002059.SZ,002060.SZ,002061.SZ,002062.SZ,002063.SZ,002064.SZ,002065.SZ,002066.SZ,002067.SZ,002068.SZ,002069.SZ,002070.SZ,002071.SZ,002072.SZ,002073.SZ,002074.SZ,002075.SZ,002076.SZ,002077.SZ,002078.SZ,002079.SZ,002080.SZ,002081.SZ,002082.SZ,002083.SZ,002084.SZ,002085.SZ,002086.SZ,002087.SZ,002088.SZ,002089.SZ,002090.SZ,002091.SZ,002092.SZ,002093.SZ,002094.SZ,002095.SZ,002096.SZ,002097.SZ,002098.SZ,002099.SZ,002100.SZ,002101.SZ,002102.SZ,002103.SZ,002104.SZ,002105.SZ,002106.SZ,002107.SZ,002108.SZ,002109.SZ,002110.SZ,002111.SZ,002112.SZ,002113.SZ,002114.SZ,002115.SZ,002116.SZ,002117.SZ,002118.SZ,002119.SZ,002120.SZ,002121.SZ,002122.SZ,002123.SZ,002124.SZ,002125.SZ,002126.SZ,002127.SZ,002128.SZ,002129.SZ,002130.SZ,002131.SZ,002132.SZ,002133.SZ,002134.SZ,002135.SZ,002136.SZ,002137.SZ,002138.SZ,002139.SZ,002140.SZ,002141.SZ,002142.SZ,002143.SZ,002144.SZ,002145.SZ,002146.SZ,002147.SZ,002148.SZ,002149.SZ,002150.SZ,002151.SZ,002152.SZ,002153.SZ,002154.SZ,002155.SZ,002156.SZ,002157.SZ,002158.SZ,002159.SZ,002160.SZ,002161.SZ,002162.SZ,002163.SZ,002164.SZ,002165.SZ,002166.SZ,002167.SZ,002168.SZ,002169.SZ,002170.SZ,002171.SZ,002172.SZ,002173.SZ,002174.SZ,002175.SZ,002176.SZ,002177.SZ,002178.SZ,002179.SZ,002180.SZ,002181.SZ,002182.SZ,002183.SZ,002184.SZ,002185.SZ,002186.SZ,002187.SZ,002188.SZ,002189.SZ,002190.SZ,002191.SZ,002192.SZ,002193.SZ,002194.SZ,002195.SZ,002196.SZ,002197.SZ,002198.SZ,002199.SZ,002200.SZ,002201.SZ,002202.SZ,002203.SZ,002204.SZ,002205.SZ,002206.SZ,002207.SZ,002208.SZ,002209.SZ,002210.SZ,002211.SZ,002212.SZ,002213.SZ,002214.SZ,002215.SZ,002216.SZ,002217.SZ,002218.SZ,002219.SZ,002220.SZ,002221.SZ,002222.SZ,002223.SZ,002224.SZ,002225.SZ,002226.SZ,002227.SZ,002228.SZ,002229.SZ,002230.SZ,002231.SZ,002232.SZ,002233.SZ,002234.SZ,002235.SZ,002236.SZ,002237.SZ,002238.SZ,002239.SZ,002240.SZ,002241.SZ,002242.SZ,002243.SZ,002244.SZ,002245.SZ,002246.SZ,002247.SZ,002248.SZ,002249.SZ,002250.SZ,002251.SZ,002252.SZ,002253.SZ,002254.SZ,002255.SZ,002256.SZ,002258.SZ,002259.SZ,002260.SZ,002261.SZ,002262.SZ,002263.SZ,002264.SZ,002265.SZ,002266.SZ,002267.SZ,002268.SZ,002269.SZ,002270.SZ,002271.SZ,002272.SZ,002273.SZ,002274.SZ,002275.SZ,002276.SZ,002277.SZ,002278.SZ,002279.SZ,002280.SZ,002281.SZ,002282.SZ,002283.SZ,002284.SZ,002285.SZ,002286.SZ,002287.SZ,002288.SZ,002289.SZ,002290.SZ,002291.SZ,002292.SZ,002293.SZ,002294.SZ,002295.SZ,002296.SZ,002297.SZ,002298.SZ,002299.SZ,002300.SZ,002301.SZ,002302.SZ,002303.SZ,002304.SZ,002305.SZ,002306.SZ,002307.SZ,002308.SZ,002309.SZ,002310.SZ,002311.SZ,002312.SZ,002313.SZ,002314.SZ,002315.SZ,002316.SZ,002317.SZ,002318.SZ,002319.SZ,002320.SZ,002321.SZ,002322.SZ,002323.SZ,002324.SZ,002325.SZ,002326.SZ,002327.SZ,002328.SZ,002329.SZ,002330.SZ,002331.SZ,002332.SZ,002333.SZ,002334.SZ,002335.SZ,002336.SZ,002337.SZ,002338.SZ,002339.SZ,002340.SZ,002341.SZ,002342.SZ,002343.SZ,002344.SZ,002345.SZ,002346.SZ,002347.SZ,002348.SZ,002349.SZ,002350.SZ,002351.SZ,002352.SZ,002353.SZ,002354.SZ,002355.SZ,002356.SZ,002357.SZ,002358.SZ,002359.SZ,002360.SZ,002361.SZ,002362.SZ,002363.SZ,002364.SZ,002365.SZ,002366.SZ,002367.SZ,002368.SZ,002369.SZ,002370.SZ,002371.SZ,002372.SZ,002373.SZ,002374.SZ,002375.SZ,002376.SZ,002377.SZ,002378.SZ,002379.SZ,002380.SZ,002381.SZ,002382.SZ,002383.SZ,002384.SZ,002385.SZ,002386.SZ,002387.SZ,002388.SZ,002389.SZ,002390.SZ,002391.SZ,002392.SZ,002393.SZ,002394.SZ,002395.SZ,002396.SZ,002397.SZ,002398.SZ,002399.SZ,002400.SZ,002401.SZ,002402.SZ,002403.SZ,002404.SZ,002405.SZ,002406.SZ,002407.SZ,002408.SZ,002409.SZ,002410.SZ,002411.SZ,002412.SZ,002413.SZ,002414.SZ,002415.SZ,002416.SZ,002417.SZ,002418.SZ,002419.SZ,002420.SZ,002421.SZ,002422.SZ,002423.SZ,002424.SZ,002425.SZ,002426.SZ,002427.SZ,002428.SZ,002429.SZ,002430.SZ,002431.SZ,002432.SZ,002433.SZ,002434.SZ,002435.SZ,002436.SZ,002437.SZ,002438.SZ,002439.SZ,002440.SZ,002441.SZ,002442.SZ,002443.SZ,002444.SZ,002445.SZ,002446.SZ,002447.SZ,002448.SZ,002449.SZ,002450.SZ,002451.SZ,002452.SZ,002453.SZ,002454.SZ,002455.SZ,002456.SZ,002457.SZ,002458.SZ,002459.SZ,002460.SZ,002461.SZ,002462.SZ,002463.SZ,002464.SZ,002465.SZ,002466.SZ,002467.SZ,002468.SZ,002469.SZ,002470.SZ,002471.SZ,002472.SZ,002473.SZ,002474.SZ,002475.SZ,002476.SZ,002477.SZ,002478.SZ,002479.SZ,002480.SZ,002481.SZ,002482.SZ,002483.SZ,002484.SZ,002485.SZ,002486.SZ,002487.SZ,002488.SZ,002489.SZ,002490.SZ,002491.SZ,002492.SZ,002493.SZ,002494.SZ,002495.SZ,002496.SZ,002497.SZ,002498.SZ,002499.SZ,002500.SZ,002501.SZ,002502.SZ,002503.SZ,002504.SZ,002505.SZ,002506.SZ,002507.SZ,002508.SZ,002509.SZ,002510.SZ,002511.SZ,002512.SZ,002513.SZ,002514.SZ,002515.SZ,002516.SZ,002517.SZ,002518.SZ,002519.SZ,002520.SZ,002521.SZ,002522.SZ,002523.SZ,002524.SZ,002526.SZ,002527.SZ,002528.SZ,002529.SZ,002530.SZ,002531.SZ,002532.SZ,002533.SZ,002534.SZ,002535.SZ,002536.SZ,002537.SZ,002538.SZ,002539.SZ,002540.SZ,002541.SZ,002542.SZ,002543.SZ,002544.SZ,002545.SZ,002546.SZ,002547.SZ,002548.SZ,002549.SZ,002550.SZ,002551.SZ,002552.SZ,002553.SZ,002554.SZ,002555.SZ,002556.SZ,002557.SZ,002558.SZ,002559.SZ,002560.SZ,002561.SZ,002562.SZ,002563.SZ,002564.SZ,002565.SZ,002566.SZ,002567.SZ,002568.SZ,002569.SZ,002570.SZ,002571.SZ,002572.SZ,002573.SZ,002574.SZ,002575.SZ,002576.SZ,002577.SZ,002578.SZ,002579.SZ,002580.SZ,002581.SZ,002582.SZ,002583.SZ,002584.SZ,002585.SZ,002586.SZ,002587.SZ,002588.SZ,002589.SZ,002590.SZ,002591.SZ,002592.SZ,002593.SZ,002594.SZ,002595.SZ,002596.SZ,002597.SZ,002598.SZ,002599.SZ,002600.SZ,002601.SZ,002602.SZ,002603.SZ,002604.SZ,002605.SZ,002606.SZ,002607.SZ,002608.SZ,002609.SZ,002610.SZ,002611.SZ,002612.SZ,002613.SZ,002614.SZ,002615.SZ,002616.SZ,002617.SZ,002618.SZ,002619.SZ,002620.SZ,002621.SZ,002622.SZ,002623.SZ,002624.SZ,002625.SZ,002626.SZ,002627.SZ,002628.SZ,002629.SZ,002630.SZ,002631.SZ,002632.SZ,002633.SZ,002634.SZ,002635.SZ,002636.SZ,002637.SZ,002638.SZ,002639.SZ,002640.SZ,002641.SZ,002642.SZ,002643.SZ,002644.SZ,002645.SZ,002646.SZ,002647.SZ,002648.SZ,002649.SZ,002650.SZ,002651.SZ,002652.SZ,002653.SZ,002654.SZ,002655.SZ,002656.SZ,002657.SZ,002658.SZ,002659.SZ,002660.SZ,002661.SZ,002662.SZ,002663.SZ,002664.SZ,002665.SZ,002666.SZ,002667.SZ,002668.SZ,002669.SZ,002670.SZ,002671.SZ,002672.SZ,002673.SZ,002674.SZ,002675.SZ,002676.SZ,002677.SZ,002678.SZ,002679.SZ,002680.SZ,002681.SZ,002682.SZ,002683.SZ,002684.SZ,002685.SZ,002686.SZ,002687.SZ,002688.SZ,002689.SZ,002690.SZ,002691.SZ,002692.SZ,002693.SZ,002694.SZ,002695.SZ,002696.SZ,002697.SZ,002698.SZ,002699.SZ,002700.SZ,002701.SZ,002702.SZ,002703.SZ,002705.SZ,002706.SZ,002707.SZ,002708.SZ,002709.SZ,002711.SZ,002712.SZ,002713.SZ,002714.SZ,002715.SZ,002716.SZ,002717.SZ,002718.SZ,002719.SZ,002721.SZ,002722.SZ,002723.SZ,002724.SZ,002725.SZ,002726.SZ,002727.SZ,002728.SZ,002729.SZ,002730.SZ,002731.SZ,002732.SZ,002733.SZ,002734.SZ,002735.SZ,002736.SZ,002737.SZ,002738.SZ,002739.SZ,002740.SZ,002741.SZ,002742.SZ,002743.SZ,002745.SZ,002746.SZ,002747.SZ,002748.SZ,002749.SZ,002750.SZ,002751.SZ,002752.SZ,002753.SZ,002755.SZ,002756.SZ,002757.SZ,002758.SZ,002759.SZ,002760.SZ,002761.SZ,002762.SZ,002763.SZ,002765.SZ,002766.SZ,002767.SZ,002768.SZ,002769.SZ,002770.SZ,002771.SZ,002772.SZ,002773.SZ,002774.SZ,002775.SZ,002776.SZ,002777.SZ,002778.SZ,002779.SZ,002780.SZ,002781.SZ,002782.SZ,002783.SZ,002785.SZ,002786.SZ,002787.SZ,002788.SZ,002789.SZ,002790.SZ,002791.SZ,002792.SZ,002793.SZ,002795.SZ,002796.SZ,002797.SZ,002798.SZ,002799.SZ,002800.SZ,002801.SZ,002802.SZ,002803.SZ,002805.SZ,002806.SZ,002807.SZ,002808.SZ,002809.SZ,002810.SZ,002811.SZ,002812.SZ,002813.SZ,002815.SZ,002816.SZ,002817.SZ,002818.SZ,002819.SZ,002820.SZ,002821.SZ,002822.SZ,002823.SZ,002824.SZ,002825.SZ,002826.SZ,002827.SZ,002828.SZ,002829.SZ,002830.SZ,002831.SZ,002832.SZ,002833.SZ,002835.SZ,002836.SZ,002837.SZ,002838.SZ,002839.SZ,002840.SZ,002841.SZ,002842.SZ,002843.SZ,002845.SZ,002846.SZ,002847.SZ,002848.SZ,002849.SZ,002850.SZ,002851.SZ,002852.SZ,002853.SZ,002855.SZ,002856.SZ,002857.SZ,002858.SZ,002859.SZ,002860.SZ,002861.SZ,002862.SZ,002863.SZ,002864.SZ,002865.SZ,002866.SZ,002867.SZ,002868.SZ,002869.SZ,002870.SZ,002871.SZ,002872.SZ,002873.SZ,002875.SZ,002876.SZ,002877.SZ,002878.SZ,002879.SZ,002880.SZ,002881.SZ,002882.SZ,002883.SZ,002884.SZ,002885.SZ,002886.SZ,002887.SZ,002888.SZ,002889.SZ,002890.SZ,002891.SZ,002892.SZ,002893.SZ,002895.SZ,002896.SZ,002897.SZ,002898.SZ,002899.SZ,002900.SZ,002901.SZ,002902.SZ,002903.SZ,002905.SZ,002906.SZ,002907.SZ,002908.SZ,002909.SZ,002910.SZ,002911.SZ,002912.SZ,002913.SZ,002915.SZ,002916.SZ,002917.SZ,002918.SZ,002919.SZ,002920.SZ,002921.SZ,002922.SZ,002923.SZ,002925.SZ,002926.SZ,002927.SZ,002928.SZ,002929.SZ,002930.SZ,002931.SZ,300001.SZ,300002.SZ,300003.SZ,300004.SZ,300005.SZ,300006.SZ,300007.SZ,300008.SZ,300009.SZ,300010.SZ,300011.SZ,300012.SZ,300013.SZ,300014.SZ,300015.SZ,300016.SZ,300017.SZ,300018.SZ,300019.SZ,300020.SZ,300021.SZ,300022.SZ,300023.SZ,300024.SZ,300025.SZ,300026.SZ,300027.SZ,300028.SZ,300029.SZ,300030.SZ,300031.SZ,300032.SZ,300033.SZ,300034.SZ,300035.SZ,300036.SZ,300037.SZ,300038.SZ,300039.SZ,300040.SZ,300041.SZ,300042.SZ,300043.SZ,300044.SZ,300045.SZ,300046.SZ,300047.SZ,300048.SZ,300049.SZ,300050.SZ,300051.SZ,300052.SZ,300053.SZ,300054.SZ,300055.SZ,300056.SZ,300057.SZ,300058.SZ,300059.SZ,300061.SZ,300062.SZ,300063.SZ,300064.SZ,300065.SZ,300066.SZ,300067.SZ,300068.SZ,300069.SZ,300070.SZ,300071.SZ,300072.SZ,300073.SZ,300074.SZ,300075.SZ,300076.SZ,300077.SZ,300078.SZ,300079.SZ,300080.SZ,300081.SZ,300082.SZ,300083.SZ,300084.SZ,300085.SZ,300086.SZ,300087.SZ,300088.SZ,300089.SZ,300090.SZ,300091.SZ,300092.SZ,300093.SZ,300094.SZ,300095.SZ,300096.SZ,300097.SZ,300098.SZ,300099.SZ,300100.SZ,300101.SZ,300102.SZ,300103.SZ,300104.SZ,300105.SZ,300106.SZ,300107.SZ,300108.SZ,300109.SZ,300110.SZ,300111.SZ,300112.SZ,300113.SZ,300114.SZ,300115.SZ,300116.SZ,300117.SZ,300118.SZ,300119.SZ,300120.SZ,300121.SZ,300122.SZ,300123.SZ,300124.SZ,300125.SZ,300126.SZ,300127.SZ,300128.SZ,300129.SZ,300130.SZ,300131.SZ,300132.SZ,300133.SZ,300134.SZ,300135.SZ,300136.SZ,300137.SZ,300138.SZ,300139.SZ,300140.SZ,300141.SZ,300142.SZ,300143.SZ,300144.SZ,300145.SZ,300146.SZ,300147.SZ,300148.SZ,300149.SZ,300150.SZ,300151.SZ,300152.SZ,300153.SZ,300154.SZ,300155.SZ,300156.SZ,300157.SZ,300158.SZ,300159.SZ,300160.SZ,300161.SZ,300162.SZ,300163.SZ,300164.SZ,300165.SZ,300166.SZ,300167.SZ,300168.SZ,300169.SZ,300170.SZ,300171.SZ,300172.SZ,300173.SZ,300174.SZ,300175.SZ,300176.SZ,300177.SZ,300178.SZ,300179.SZ,300180.SZ,300181.SZ,300182.SZ,300183.SZ,300184.SZ,300185.SZ,300187.SZ,300188.SZ,300189.SZ,300190.SZ,300191.SZ,300192.SZ,300193.SZ,300194.SZ,300195.SZ,300196.SZ,300197.SZ,300198.SZ,300199.SZ,300200.SZ,300201.SZ,300202.SZ,300203.SZ,300204.SZ,300205.SZ,300206.SZ,300207.SZ,300208.SZ,300209.SZ,300210.SZ,300211.SZ,300212.SZ,300213.SZ,300214.SZ,300215.SZ,300216.SZ,300217.SZ,300218.SZ,300219.SZ,300220.SZ,300221.SZ,300222.SZ,300223.SZ,300224.SZ,300225.SZ,300226.SZ,300227.SZ,300228.SZ,300229.SZ,300230.SZ,300231.SZ,300232.SZ,300233.SZ,300234.SZ,300235.SZ,300236.SZ,300237.SZ,300238.SZ,300239.SZ,300240.SZ,300241.SZ,300242.SZ,300243.SZ,300244.SZ,300245.SZ,300246.SZ,300247.SZ,300248.SZ,300249.SZ,300250.SZ,300251.SZ,300252.SZ,300253.SZ,300254.SZ,300255.SZ,300256.SZ,300257.SZ,300258.SZ,300259.SZ,300260.SZ,300261.SZ,300262.SZ,300263.SZ,300264.SZ,300265.SZ,300266.SZ,300267.SZ,300268.SZ,300269.SZ,300270.SZ,300271.SZ,300272.SZ,300273.SZ,300274.SZ,300275.SZ,300276.SZ,300277.SZ,300278.SZ,300279.SZ,300280.SZ,300281.SZ,300282.SZ,300283.SZ,300284.SZ,300285.SZ,300286.SZ,300287.SZ,300288.SZ,300289.SZ,300290.SZ,300291.SZ,300292.SZ,300293.SZ,300294.SZ,300295.SZ,300296.SZ,300297.SZ,300298.SZ,300299.SZ,300300.SZ,300301.SZ,300302.SZ,300303.SZ,300304.SZ,300305.SZ,300306.SZ,300307.SZ,300308.SZ,300309.SZ,300310.SZ,300311.SZ,300312.SZ,300313.SZ,300314.SZ,300315.SZ,300316.SZ,300317.SZ,300318.SZ,300319.SZ,300320.SZ,300321.SZ,300322.SZ,300323.SZ,300324.SZ,300325.SZ,300326.SZ,300327.SZ,300328.SZ,300329.SZ,300330.SZ,300331.SZ,300332.SZ,300333.SZ,300334.SZ,300335.SZ,300336.SZ,300337.SZ,300338.SZ,300339.SZ,300340.SZ,300341.SZ,300342.SZ,300343.SZ,300344.SZ,300345.SZ,300346.SZ,300347.SZ,300348.SZ,300349.SZ,300350.SZ,300351.SZ,300352.SZ,300353.SZ,300354.SZ,300355.SZ,300356.SZ,300357.SZ,300358.SZ,300359.SZ,300360.SZ,300362.SZ,300363.SZ,300364.SZ,300365.SZ,300366.SZ,300367.SZ,300368.SZ,300369.SZ,300370.SZ,300371.SZ,300373.SZ,300374.SZ,300375.SZ,300376.SZ,300377.SZ,300378.SZ,300379.SZ,300380.SZ,300381.SZ,300382.SZ,300383.SZ,300384.SZ,300385.SZ,300386.SZ,300387.SZ,300388.SZ,300389.SZ,300390.SZ,300391.SZ,300392.SZ,300393.SZ,300394.SZ,300395.SZ,300396.SZ,300397.SZ,300398.SZ,300399.SZ,300400.SZ,300401.SZ,300402.SZ,300403.SZ,300404.SZ,300405.SZ,300406.SZ,300407.SZ,300408.SZ,300409.SZ,300410.SZ,300411.SZ,300412.SZ,300413.SZ,300414.SZ,300415.SZ,300416.SZ,300417.SZ,300418.SZ,300419.SZ,300420.SZ,300421.SZ,300422.SZ,300423.SZ,300424.SZ,300425.SZ,300426.SZ,300427.SZ,300428.SZ,300429.SZ,300430.SZ,300431.SZ,300432.SZ,300433.SZ,300434.SZ,300435.SZ,300436.SZ,300437.SZ,300438.SZ,300439.SZ,300440.SZ,300441.SZ,300442.SZ,300443.SZ,300444.SZ,300445.SZ,300446.SZ,300447.SZ,300448.SZ,300449.SZ,300450.SZ,300451.SZ,300452.SZ,300453.SZ,300455.SZ,300456.SZ,300457.SZ,300458.SZ,300459.SZ,300460.SZ,300461.SZ,300462.SZ,300463.SZ,300464.SZ,300465.SZ,300466.SZ,300467.SZ,300468.SZ,300469.SZ,300470.SZ,300471.SZ,300472.SZ,300473.SZ,300474.SZ,300475.SZ,300476.SZ,300477.SZ,300478.SZ,300479.SZ,300480.SZ,300481.SZ,300482.SZ,300483.SZ,300484.SZ,300485.SZ,300486.SZ,300487.SZ,300488.SZ,300489.SZ,300490.SZ,300491.SZ,300492.SZ,300493.SZ,300494.SZ,300495.SZ,300496.SZ,300497.SZ,300498.SZ,300499.SZ,300500.SZ,300501.SZ,300502.SZ,300503.SZ,300504.SZ,300505.SZ,300506.SZ,300507.SZ,300508.SZ,300509.SZ,300510.SZ,300511.SZ,300512.SZ,300513.SZ,300514.SZ,300515.SZ,300516.SZ,300517.SZ,300518.SZ,300519.SZ,300520.SZ,300521.SZ,300522.SZ,300523.SZ,300525.SZ,300526.SZ,300527.SZ,300528.SZ,300529.SZ,300530.SZ,300531.SZ,300532.SZ,300533.SZ,300534.SZ,300535.SZ,300536.SZ,300537.SZ,300538.SZ,300539.SZ,300540.SZ,300541.SZ,300542.SZ,300543.SZ,300545.SZ,300546.SZ,300547.SZ,300548.SZ,300549.SZ,300550.SZ,300551.SZ,300552.SZ,300553.SZ,300554.SZ,300555.SZ,300556.SZ,300557.SZ,300558.SZ,300559.SZ,300560.SZ,300561.SZ,300562.SZ,300563.SZ,300565.SZ,300566.SZ,300567.SZ,300568.SZ,300569.SZ,300570.SZ,300571.SZ,300572.SZ,300573.SZ,300575.SZ,300576.SZ,300577.SZ,300578.SZ,300579.SZ,300580.SZ,300581.SZ,300582.SZ,300583.SZ,300584.SZ,300585.SZ,300586.SZ,300587.SZ,300588.SZ,300589.SZ,300590.SZ,300591.SZ,300592.SZ,300593.SZ,300595.SZ,300596.SZ,300597.SZ,300598.SZ,300599.SZ,300600.SZ,300601.SZ,300602.SZ,300603.SZ,300604.SZ,300605.SZ,300606.SZ,300607.SZ,300608.SZ,300609.SZ,300610.SZ,300611.SZ,300612.SZ,300613.SZ,300615.SZ,300616.SZ,300617.SZ,300618.SZ,300619.SZ,300620.SZ,300621.SZ,300622.SZ,300623.SZ,300624.SZ,300625.SZ,300626.SZ,300627.SZ,300628.SZ,300629.SZ,300630.SZ,300631.SZ,300632.SZ,300633.SZ,300634.SZ,300635.SZ,300636.SZ,300637.SZ,300638.SZ,300639.SZ,300640.SZ,300641.SZ,300642.SZ,300643.SZ,300644.SZ,300645.SZ,300647.SZ,300648.SZ,300649.SZ,300650.SZ,300651.SZ,300652.SZ,300653.SZ,300654.SZ,300655.SZ,300656.SZ,300657.SZ,300658.SZ,300659.SZ,300660.SZ,300661.SZ,300662.SZ,300663.SZ,300664.SZ,300665.SZ,300666.SZ,300667.SZ,300668.SZ,300669.SZ,300670.SZ,300671.SZ,300672.SZ,300673.SZ,300675.SZ,300676.SZ,300677.SZ,300678.SZ,300679.SZ,300680.SZ,300681.SZ,300682.SZ,300683.SZ,300684.SZ,300685.SZ,300686.SZ,300687.SZ,300688.SZ,300689.SZ,300690.SZ,300691.SZ,300692.SZ,300693.SZ,300695.SZ,300696.SZ,300697.SZ,300698.SZ,300699.SZ,300700.SZ,300701.SZ,300702.SZ,300703.SZ,300705.SZ,300706.SZ,300707.SZ,300708.SZ,300709.SZ,300710.SZ,300711.SZ,300712.SZ,300713.SZ,300715.SZ,300716.SZ,300717.SZ,300718.SZ,300719.SZ,300720.SZ,300721.SZ,300722.SZ,300723.SZ,300725.SZ,300726.SZ,300727.SZ,300729.SZ,300730.SZ,300731.SZ,300732.SZ,300733.SZ,300735.SZ,300736.SZ,300737.SZ,300738.SZ,300739.SZ,300740.SZ,300741.SZ,600000.SH,600004.SH,600006.SH,600007.SH,600008.SH,600009.SH,600010.SH,600011.SH,600012.SH,600015.SH,600016.SH,600017.SH,600018.SH,600019.SH,600020.SH,600021.SH,600022.SH,600023.SH,600025.SH,600026.SH,600027.SH,600028.SH,600029.SH,600030.SH,600031.SH,600033.SH,600035.SH,600036.SH,600037.SH,600038.SH,600039.SH,600048.SH,600050.SH,600051.SH,600052.SH,600053.SH,600054.SH,600055.SH,600056.SH,600057.SH,600058.SH,600059.SH,600060.SH,600061.SH,600062.SH,600063.SH,600064.SH,600066.SH,600067.SH,600068.SH,600069.SH,600070.SH,600071.SH,600072.SH,600073.SH,600074.SH,600075.SH,600076.SH,600077.SH,600078.SH,600079.SH,600080.SH,600081.SH,600082.SH,600083.SH,600084.SH,600085.SH,600086.SH,600088.SH,600089.SH,600090.SH,600091.SH,600093.SH,600094.SH,600095.SH,600096.SH,600097.SH,600098.SH,600099.SH,600100.SH,600101.SH,600103.SH,600104.SH,600105.SH,600106.SH,600107.SH,600108.SH,600109.SH,600110.SH,600111.SH,600112.SH,600113.SH,600114.SH,600115.SH,600116.SH,600117.SH,600118.SH,600119.SH,600120.SH,600121.SH,600122.SH,600123.SH,600125.SH,600126.SH,600127.SH,600128.SH,600129.SH,600130.SH,600131.SH,600132.SH,600133.SH,600135.SH,600136.SH,600137.SH,600138.SH,600139.SH,600141.SH,600143.SH,600145.SH,600146.SH,600148.SH,600149.SH,600150.SH,600151.SH,600152.SH,600153.SH,600155.SH,600156.SH,600157.SH,600158.SH,600159.SH,600160.SH,600161.SH,600162.SH,600163.SH,600165.SH,600166.SH,600167.SH,600168.SH,600169.SH,600170.SH,600171.SH,600172.SH,600173.SH,600175.SH,600176.SH,600177.SH,600178.SH,600179.SH,600180.SH,600182.SH,600183.SH,600184.SH,600185.SH,600186.SH,600187.SH,600188.SH,600189.SH,600190.SH,600191.SH,600192.SH,600193.SH,600195.SH,600196.SH,600197.SH,600198.SH,600199.SH,600200.SH,600201.SH,600202.SH,600203.SH,600206.SH,600207.SH,600208.SH,600209.SH,600210.SH,600211.SH,600212.SH,600213.SH,600215.SH,600216.SH,600217.SH,600218.SH,600219.SH,600220.SH,600221.SH,600222.SH,600223.SH,600225.SH,600226.SH,600227.SH,600228.SH,600229.SH,600230.SH,600231.SH,600232.SH,600233.SH,600234.SH,600235.SH,600236.SH,600237.SH,600238.SH,600239.SH,600240.SH,600241.SH,600242.SH,600243.SH,600246.SH,600247.SH,600248.SH,600249.SH,600250.SH,600251.SH,600252.SH,600255.SH,600256.SH,600257.SH,600258.SH,600259.SH,600260.SH,600261.SH,600262.SH,600265.SH,600266.SH,600267.SH,600268.SH,600269.SH,600270.SH,600271.SH,600272.SH,600273.SH,600275.SH,600276.SH,600277.SH,600278.SH,600279.SH,600280.SH,600281.SH,600282.SH,600283.SH,600284.SH,600285.SH,600287.SH,600288.SH,600289.SH,600290.SH,600291.SH,600292.SH,600293.SH,600295.SH,600297.SH,600298.SH,600299.SH,600300.SH,600301.SH,600302.SH,600303.SH,600305.SH,600306.SH,600307.SH,600308.SH,600309.SH,600310.SH,600311.SH,600312.SH,600313.SH,600315.SH,600316.SH,600317.SH,600318.SH,600319.SH,600320.SH,600321.SH,600322.SH,600323.SH,600325.SH,600326.SH,600327.SH,600328.SH,600329.SH,600330.SH,600331.SH,600332.SH,600333.SH,600335.SH,600336.SH,600337.SH,600338.SH,600339.SH,600340.SH,600343.SH,600345.SH,600346.SH,600348.SH,600350.SH,600351.SH,600352.SH,600353.SH,600354.SH,600355.SH,600356.SH,600358.SH,600359.SH,600360.SH,600361.SH,600362.SH,600363.SH,600365.SH,600366.SH,600367.SH,600368.SH,600369.SH,600370.SH,600371.SH,600372.SH,600373.SH,600375.SH,600376.SH,600377.SH,600378.SH,600379.SH,600380.SH,600381.SH,600382.SH,600383.SH,600385.SH,600386.SH,600387.SH,600388.SH,600389.SH,600390.SH,600391.SH,600392.SH,600393.SH,600395.SH,600396.SH,600397.SH,600398.SH,600399.SH,600400.SH,600401.SH,600403.SH,600405.SH,600406.SH,600408.SH,600409.SH,600410.SH,600415.SH,600416.SH,600418.SH,600419.SH,600420.SH,600421.SH,600422.SH,600423.SH,600425.SH,600426.SH,600428.SH,600429.SH,600432.SH,600433.SH,600435.SH,600436.SH,600438.SH,600439.SH,600444.SH,600446.SH,600448.SH,600449.SH,600452.SH,600455.SH,600456.SH,600458.SH,600459.SH,600460.SH,600461.SH,600462.SH,600463.SH,600466.SH,600467.SH,600468.SH,600469.SH,600470.SH,600475.SH,600476.SH,600477.SH,600478.SH,600479.SH,600480.SH,600481.SH,600482.SH,600483.SH,600485.SH,600486.SH,600487.SH,600488.SH,600489.SH,600490.SH,600491.SH,600493.SH,600495.SH,600496.SH,600497.SH,600498.SH,600499.SH,600500.SH,600501.SH,600502.SH,600503.SH,600505.SH,600506.SH,600507.SH,600508.SH,600509.SH,600510.SH,600511.SH,600512.SH,600513.SH,600515.SH,600516.SH,600517.SH,600518.SH,600519.SH,600520.SH,600521.SH,600522.SH,600523.SH,600525.SH,600526.SH,600527.SH,600528.SH,600529.SH,600530.SH,600531.SH,600532.SH,600533.SH,600535.SH,600536.SH,600537.SH,600538.SH,600539.SH,600540.SH,600543.SH,600545.SH,600546.SH,600547.SH,600548.SH,600549.SH,600550.SH,600551.SH,600552.SH,600555.SH,600556.SH,600557.SH,600558.SH,600559.SH,600560.SH,600561.SH,600562.SH,600563.SH,600565.SH,600566.SH,600567.SH,600568.SH,600569.SH,600570.SH,600571.SH,600572.SH,600573.SH,600575.SH,600576.SH,600577.SH,600578.SH,600579.SH,600580.SH,600581.SH,600582.SH,600583.SH,600584.SH,600585.SH,600586.SH,600587.SH,600588.SH,600589.SH,600590.SH,600592.SH,600593.SH,600594.SH,600595.SH,600596.SH,600597.SH,600598.SH,600599.SH,600600.SH,600601.SH,600602.SH,600603.SH,600604.SH,600605.SH,600606.SH,600608.SH,600609.SH,600610.SH,600611.SH,600612.SH,600613.SH,600614.SH,600615.SH,600616.SH,600617.SH,600618.SH,600619.SH,600620.SH,600621.SH,600622.SH,600623.SH,600624.SH,600626.SH,600628.SH,600629.SH,600630.SH,600633.SH,600634.SH,600635.SH,600636.SH,600637.SH,600638.SH,600639.SH,600640.SH,600641.SH,600642.SH,600643.SH,600644.SH,600645.SH,600647.SH,600648.SH,600649.SH,600650.SH,600651.SH,600652.SH,600653.SH,600654.SH,600655.SH,600657.SH,600658.SH,600660.SH,600661.SH,600662.SH,600663.SH,600664.SH,600665.SH,600666.SH,600667.SH,600668.SH,600671.SH,600673.SH,600674.SH,600675.SH,600676.SH,600677.SH,600678.SH,600679.SH,600680.SH,600681.SH,600682.SH,600683.SH,600684.SH,600685.SH,600686.SH,600687.SH,600688.SH,600689.SH,600690.SH,600691.SH,600692.SH,600693.SH,600694.SH,600695.SH,600696.SH,600697.SH,600698.SH,600699.SH,600701.SH,600702.SH,600703.SH,600704.SH,600705.SH,600706.SH,600707.SH,600708.SH,600710.SH,600711.SH,600712.SH,600713.SH,600714.SH,600715.SH,600716.SH,600717.SH,600718.SH,600719.SH,600720.SH,600721.SH,600722.SH,600723.SH,600724.SH,600725.SH,600726.SH,600727.SH,600728.SH,600729.SH,600730.SH,600731.SH,600732.SH,600733.SH,600734.SH,600735.SH,600736.SH,600737.SH,600738.SH,600739.SH,600740.SH,600741.SH,600742.SH,600743.SH,600744.SH,600745.SH,600746.SH,600747.SH,600748.SH,600749.SH,600750.SH,600751.SH,600753.SH,600754.SH,600755.SH,600756.SH,600757.SH,600758.SH,600759.SH,600760.SH,600761.SH,600763.SH,600764.SH,600765.SH,600766.SH,600767.SH,600768.SH,600769.SH,600770.SH,600771.SH,600773.SH,600774.SH,600775.SH,600776.SH,600777.SH,600778.SH,600779.SH,600780.SH,600781.SH,600782.SH,600783.SH,600784.SH,600785.SH,600787.SH,600789.SH,600790.SH,600791.SH,600792.SH,600793.SH,600794.SH,600795.SH,600796.SH,600797.SH,600798.SH,600800.SH,600801.SH,600802.SH,600803.SH,600804.SH,600805.SH,600806.SH,600807.SH,600808.SH,600809.SH,600810.SH,600811.SH,600812.SH,600814.SH,600815.SH,600816.SH,600817.SH,600818.SH,600819.SH,600820.SH,600821.SH,600822.SH,600823.SH,600824.SH,600825.SH,600826.SH,600827.SH,600828.SH,600829.SH,600830.SH,600831.SH,600833.SH,600834.SH,600835.SH,600836.SH,600837.SH,600838.SH,600839.SH,600841.SH,600843.SH,600844.SH,600845.SH,600846.SH,600847.SH,600848.SH,600850.SH,600851.SH,600853.SH,600854.SH,600855.SH,600856.SH,600857.SH,600858.SH,600859.SH,600860.SH,600861.SH,600862.SH,600863.SH,600864.SH,600865.SH,600866.SH,600867.SH,600868.SH,600869.SH,600870.SH,600871.SH,600872.SH,600873.SH,600874.SH,600875.SH,600876.SH,600877.SH,600879.SH,600880.SH,600881.SH,600882.SH,600883.SH,600884.SH,600885.SH,600886.SH,600887.SH,600888.SH,600889.SH,600890.SH,600891.SH,600892.SH,600893.SH,600894.SH,600895.SH,600896.SH,600897.SH,600898.SH,600900.SH,600901.SH,600903.SH,600908.SH,600909.SH,600917.SH,600919.SH,600926.SH,600929.SH,600933.SH,600936.SH,600939.SH,600958.SH,600959.SH,600960.SH,600961.SH,600962.SH,600963.SH,600965.SH,600966.SH,600967.SH,600969.SH,600970.SH,600971.SH,600973.SH,600975.SH,600976.SH,600977.SH,600978.SH,600979.SH,600980.SH,600981.SH,600982.SH,600983.SH,600984.SH,600985.SH,600986.SH,600987.SH,600988.SH,600990.SH,600992.SH,600993.SH,600995.SH,600996.SH,600997.SH,600998.SH,600999.SH,601000.SH,601001.SH,601002.SH,601003.SH,601005.SH,601006.SH,601007.SH,601008.SH,601009.SH,601010.SH,601011.SH,601012.SH,601015.SH,601016.SH,601018.SH,601019.SH,601020.SH,601021.SH,601028.SH,601038.SH,601058.SH,601069.SH,601086.SH,601088.SH,601098.SH,601099.SH,601100.SH,601101.SH,601106.SH,601107.SH,601108.SH,601111.SH,601113.SH,601116.SH,601117.SH,601118.SH,601126.SH,601127.SH,601128.SH,601137.SH,601139.SH,601155.SH,601158.SH,601163.SH,601166.SH,601168.SH,601169.SH,601177.SH,601179.SH,601186.SH,601188.SH,601198.SH,601199.SH,601200.SH,601208.SH,601211.SH,601212.SH,601216.SH,601218.SH,601222.SH,601225.SH,601226.SH,601228.SH,601229.SH,601231.SH,601233.SH,601238.SH,601258.SH,601288.SH,601311.SH,601318.SH,601326.SH,601328.SH,601333.SH,601336.SH,601339.SH,601360.SH,601366.SH,601368.SH,601369.SH,601375.SH,601377.SH,601388.SH,601390.SH,601398.SH,601500.SH,601515.SH,601518.SH,601519.SH,601555.SH,601558.SH,601566.SH,601567.SH,601579.SH,601588.SH,601595.SH,601599.SH,601600.SH,601601.SH,601607.SH,601608.SH,601611.SH,601616.SH,601618.SH,601619.SH,601628.SH,601633.SH,601636.SH,601666.SH,601668.SH,601669.SH,601677.SH,601678.SH,601688.SH,601689.SH,601699.SH,601700.SH,601717.SH,601718.SH,601727.SH,601766.SH,601777.SH,601788.SH,601789.SH,601798.SH,601799.SH,601800.SH,601801.SH,601808.SH,601811.SH,601818.SH,601828.SH,601838.SH,601857.SH,601858.SH,601866.SH,601872.SH,601877.SH,601878.SH,601880.SH,601881.SH,601882.SH,601886.SH,601888.SH,601890.SH,601898.SH,601899.SH,601900.SH,601901.SH,601908.SH,601918.SH,601919.SH,601928.SH,601929.SH,601933.SH,601939.SH,601949.SH,601952.SH,601958.SH,601965.SH,601966.SH,601968.SH,601969.SH,601985.SH,601988.SH,601989.SH,601991.SH,601992.SH,601996.SH,601997.SH,601998.SH,601999.SH,603000.SH,603001.SH,603002.SH,603003.SH,603005.SH,603006.SH,603007.SH,603008.SH,603009.SH,603010.SH,603011.SH,603012.SH,603015.SH,603016.SH,603017.SH,603018.SH,603019.SH,603020.SH,603021.SH,603022.SH,603023.SH,603025.SH,603026.SH,603027.SH,603028.SH,603029.SH,603030.SH,603031.SH,603032.SH,603033.SH,603035.SH,603036.SH,603037.SH,603038.SH,603039.SH,603040.SH,603041.SH,603042.SH,603043.SH,603050.SH,603055.SH,603056.SH,603058.SH,603059.SH,603060.SH,603063.SH,603066.SH,603067.SH,603069.SH,603076.SH,603077.SH,603078.SH,603079.SH,603080.SH,603081.SH,603083.SH,603085.SH,603086.SH,603088.SH,603089.SH,603090.SH,603096.SH,603098.SH,603099.SH,603100.SH,603101.SH,603103.SH,603106.SH,603108.SH,603110.SH,603111.SH,603113.SH,603116.SH,603117.SH,603118.SH,603123.SH,603126.SH,603127.SH,603128.SH,603129.SH,603131.SH,603133.SH,603136.SH,603138.SH,603139.SH,603156.SH,603157.SH,603158.SH,603159.SH,603160.SH,603161.SH,603165.SH,603166.SH,603167.SH,603168.SH,603169.SH,603177.SH,603178.SH,603179.SH,603180.SH,603181.SH,603183.SH,603186.SH,603188.SH,603189.SH,603196.SH,603197.SH,603198.SH,603199.SH,603200.SH,603203.SH,603208.SH,603214.SH,603218.SH,603222.SH,603223.SH,603225.SH,603226.SH,603227.SH,603228.SH,603229.SH,603232.SH,603233.SH,603238.SH,603239.SH,603258.SH,603260.SH,603266.SH,603268.SH,603269.SH,603277.SH,603278.SH,603283.SH,603286.SH,603288.SH,603289.SH,603298.SH,603299.SH,603300.SH,603303.SH,603305.SH,603306.SH,603308.SH,603309.SH,603311.SH,603313.SH,603315.SH,603316.SH,603318.SH,603319.SH,603320.SH,603321.SH,603322.SH,603323.SH,603326.SH,603328.SH,603329.SH,603330.SH,603331.SH,603333.SH,603335.SH,603336.SH,603337.SH,603338.SH,603339.SH,603345.SH,603355.SH,603356.SH,603357.SH,603358.SH,603359.SH,603360.SH,603363.SH,603365.SH,603366.SH,603367.SH,603368.SH,603369.SH,603377.SH,603378.SH,603380.SH,603383.SH,603385.SH,603386.SH,603387.SH,603388.SH,603389.SH,603393.SH,603396.SH,603398.SH,603399.SH,603416.SH,603421.SH,603429.SH,603444.SH,603456.SH,603458.SH,603466.SH,603477.SH,603488.SH,603496.SH,603499.SH,603500.SH,603501.SH,603505.SH,603506.SH,603507.SH,603508.SH,603515.SH,603516.SH,603517.SH,603518.SH,603519.SH,603520.SH,603527.SH,603528.SH,603533.SH,603535.SH,603536.SH,603538.SH,603555.SH,603556.SH,603557.SH,603558.SH,603559.SH,603566.SH,603567.SH,603568.SH,603569.SH,603577.SH,603578.SH,603579.SH,603580.SH,603585.SH,603586.SH,603588.SH,603589.SH,603595.SH,603598.SH,603599.SH,603600.SH,603601.SH,603602.SH,603603.SH,603605.SH,603606.SH,603607.SH,603608.SH,603609.SH,603611.SH,603612.SH,603615.SH,603616.SH,603617.SH,603618.SH,603619.SH,603626.SH,603628.SH,603630.SH,603633.SH,603636.SH,603637.SH,603638.SH,603639.SH,603648.SH,603655.SH,603656.SH,603658.SH,603659.SH,603660.SH,603661.SH,603663.SH,603665.SH,603667.SH,603668.SH,603669.SH,603676.SH,603677.SH,603678.SH,603679.SH,603680.SH,603683.SH,603685.SH,603686.SH,603688.SH,603689.SH,603690.SH,603696.SH,603698.SH,603699.SH,603701.SH,603703.SH,603707.SH,603708.SH,603709.SH,603711.SH,603712.SH,603716.SH,603717.SH,603718.SH,603721.SH,603722.SH,603725.SH,603726.SH,603727.SH,603728.SH,603729.SH,603730.SH,603737.SH,603738.SH,603757.SH,603758.SH,603766.SH,603767.SH,603768.SH,603776.SH,603777.SH,603778.SH,603779.SH,603787.SH,603788.SH,603789.SH,603797.SH,603798.SH,603799.SH,603800.SH,603801.SH,603803.SH,603806.SH,603808.SH,603809.SH,603811.SH,603813.SH,603816.SH,603817.SH,603818.SH,603819.SH,603822.SH,603823.SH,603825.SH,603826.SH,603828.SH,603829.SH,603833.SH,603838.SH,603839.SH,603843.SH,603848.SH,603855.SH,603856.SH,603858.SH,603859.SH,603860.SH,603861.SH,603866.SH,603868.SH,603869.SH,603871.SH,603877.SH,603878.SH,603879.SH,603880.SH,603881.SH,603882.SH,603883.SH,603885.SH,603886.SH,603887.SH,603888.SH,603889.SH,603890.SH,603895.SH,603896.SH,603897.SH,603898.SH,603899.SH,603900.SH,603901.SH,603903.SH,603906.SH,603908.SH,603909.SH,603912.SH,603916.SH,603917.SH,603918.SH,603919.SH,603920.SH,603922.SH,603926.SH,603928.SH,603929.SH,603933.SH,603936.SH,603937.SH,603938.SH,603939.SH,603955.SH,603958.SH,603959.SH,603960.SH,603963.SH,603966.SH,603968.SH,603969.SH,603970.SH,603976.SH,603977.SH,603978.SH,603979.SH,603980.SH,603985.SH,603986.SH,603987.SH,603988.SH,603989.SH,603990.SH,603991.SH,603993.SH,603996.SH,603997.SH,603998.SH,603999.SH","MACD", "TradeDate=%s, N1=12, N2=26, N3=9, Macd=3, AdjustFlag=1, Period=1"%date).Data

	with open("shareData.json", "r") as share_file:
		shares=json.load(share_file)
	with open("macdData.json", "r") as macd_file:
		macd=json.load(macd_file)

	for share in shares:
		macd[share]+=data[share]

	with open("macdData.json", "w") as macd_file:
		macd_file.write(json.dumps(macd))

login()
addMACD()