# -*- encoding=utf8 -*-
__author__ = "qiuyunxia"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# dev=connect_device("android:///988bdc454835315257")

# dev.stop_app("com.tencent.mm")
# dev.start_app("com.tencent.mm")
stop_app("com.tencent.mm")
start_app("com.tencent.mm")
sleep(2.0)

touch(Template(r"tpl1547971115581.png", record_pos=(0.344, 0.825), resolution=(1080, 2220)))

wait(Template(r"tpl1547971141224.png", record_pos=(-0.104, -0.671), resolution=(1080, 2220)))

poco(text="收藏").click()
poco(text="http://jssdk-test.rayjump.com/online_jssdk/nv.html").click()
wait(Template(r"tpl1547971246616.png", record_pos=(-0.341, -0.955), resolution=(1080, 2220)))
poco("com.tencent.mm:id/bpg").click()
wait(Template(r"tpl1547971298143.png", record_pos=(-0.13, -0.769), resolution=(1080, 2220)))

touch(Template(r"tpl1547971519018.png", record_pos=(-0.041, -0.429), resolution=(1080, 2220)))



snapshot()
snapshot()
poco("download").click()
sleep(2.0)
snapshot()

snapshot()









