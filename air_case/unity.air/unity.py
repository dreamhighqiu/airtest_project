# -*- encoding=utf8 -*-
__author__ = "qiuyunxia"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# dev=connect_device("android:///988bdc454835315257")
                                      
# dev.stop_app("com.unity3d.ads.example.creative")
#
# dev.start_app("com.unity3d.ads.example.creative")

stop_app("com.unity3d.ads.example.creative")

start_app("com.unity3d.ads.example.creative")



# poco("com.unity3d.ads.example.creative:id/unityads_example_gameid_edit").set_text("https://playable-portal.s3.amazonaws.com/qa_task/t3795/v2/fluffyfall_plj0zp/fluffyfall_plj0zp.html")

# poco("com.unity3d.ads.example.creative:id/unityads_example_gameid_edit").click()


poco("com.unity3d.ads.example.creative:id/unityads_example_initialize_button").click()
 
snapshot()
poco("com.unity3d.ads.example.creative:id/unityads_example_interstitial_button").click()
sleep(4.0)
snapshot()
snapshot()

wait(Template(r"tpl1547966723580.png", record_pos=(0.005, 0.828), resolution=(1080, 2220)))
touch(Template(r"tpl1547966742057.png", record_pos=(0.005, 0.847), resolution=(1080, 2220)))


sleep(1.0)
snapshot()




                   
    
                   
         



