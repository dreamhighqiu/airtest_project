# -*- encoding=utf8 -*-
__author__ = "qiuyunxia"

from airtest.core.api import *

auto_setup(__file__)

import time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# dev=connect_device("android:///988bdc454835315257")
#stop_app("com.mintegral.sdk.demo")
#start_app("com.mintegral.sdk.demo")
stop_app("com.mintegral.sdk.demo")
start_app("com.mintegral.sdk.demo")
poco("com.mintegral.sdk.demo:id/mintegral_demo_lv_ad_list").offspring("com.mintegral.sdk.demo:id/mintegral_demo_item_iv_big").click()
poco("android:id/content").offspring("com.mintegral.sdk.demo:id/mintegral_demo_gv_native_list").offspring("com.mintegral.sdk.demo:id/mintegral_demo_iv_name").click()
poco("com.mintegral.sdk.demo:id/btPreNative").click()
poco("com.mintegral.sdk.demo:id/btNative").click()
poco("com.mintegral.sdk.demo:id/mintegral_demo_iv_image").click()

snapshot()
snapshot()
home()






