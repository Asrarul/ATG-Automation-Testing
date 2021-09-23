from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

# Desired Capabilities to start the app in the Appium Server
capabilities = {
    
    # Mobile OS platform name
    "platformName": "Android",
    
    # App Activity name to lauch an activity in appium server
    "appActivity": "com.atg.world.activity.SplashActivity",
    
    # Duration to wait for the app to launch 
    "appWaitDuration": "50000",

    # Time given to the app for Execution
    "appExecTimeout": "50000",

    # Maximum waiting time for the appium server to listen the device
    "uiautomator2ServerLaunchTimeout": "50000",

    # Maximum waiting time for the appium server to install on the device
    "uiautomator2ServerInstallTimeout": "50000",

    # The whole Java package name for this Native android app
    "appPackage": "com.ATG.World",

    # The name of the Mobile device
    "deviceName": "Android Simulator",

    # Access point of the driver
    "driver": "http://localhost:4723/wd/hub"
}

# Connecting the driver to the appium server
driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
driver.implicitly_wait(30)

# To click get started
GetStarted = driver.find_element_by_id("com.ATG.World:id/getStartedTv")
GetStarted.click()

# To click sign in
login_a = driver.find_element_by_id("com.ATG.World:id/login_email")
login_a.click()

# Providing the E-mail id 
email = driver.find_element_by_id("com.ATG.World:id/email")
email.send_keys("wiz_saurabh@rediffmail.com")

# Providing the Password
password = driver.find_element_by_id("com.ATG.World:id/password")
password.send_keys("Pass@123")

# To click Sign in Button 
sign_in = driver.find_element_by_id("com.ATG.World:id/email_sign_in_button")
sign_in.click()
print("Logged in Successfully")

# Starting Main activity
driver.start_activity("com.ATG.World", "com.atg.world.activity.MainActivity")

# To Tap Got it
TouchAction(driver).tap(x=98, y=483).perform()
sleep(2)
TouchAction(driver).tap(x=93, y=378).perform()

# To Click Pencil button
el1 = driver.find_element_by_id("com.ATG.World:id/fab")
el1.click()

# To click Post Image option
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.ImageView")
el2.click()

# To click Choose from gallery option
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]")
el1.click()
print("\n\nSuccessfully started Posting image")

# To Switch the activity to Gallery app's activity
driver.current_activity

# To Select the image
sleep(2)
TouchAction(driver).tap(x=93, y=161).perform()
print("\n\nImage selected Successfully")

# Switching back to our ATG app's activity
driver.current_activity

# To provide caption for the image
Caption = driver.find_element_by_id("com.ATG.World:id/postCaption")
Caption.send_keys("ATG - Professional Networking Platform")

# To Click the Post Button
postImage = driver.find_element_by_id("com.ATG.World:id/toolbar_post_action")
postImage.click()
print("\n\nPosted image Successfully")