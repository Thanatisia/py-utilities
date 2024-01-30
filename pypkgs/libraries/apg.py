"""
Android Project Generator class module
"""
import os
import sys

class AndroidProjectGenerator():
    """
    Main Android Project Generator class
    """
    def __init__(self, apg_Object):
        self.apg_Object = apg_Object # The APG[Operating System] class object instance
        self.settings = apg_Object.settings # Retrieve the settings from the APG[System] class
        self.apg_Utils = APGUtils()

    def set_android_Environment(self, setting_key, new_Value):
        """
        Set and overwrite Android environment settings

        :: Params
        - setting_key : Specify the setting you want to change
            + ANDROID_HOME : Set the Android SDK root directory
            + ANDROID_USER_HOME : Set the Android SDK user home directory
            + ANDROID_EMULATOR_HOME : Set the home path of the Android SDK official Emulator
            + ANDROID_AVD_HOME : Set the home path of the Android SDK Virtual Device

        - new_Value : Specify the new value to overwrite
            Type: String
        """
        self.settings["env"][setting_key] = new_Value

    def set_android_Tools(self, setting_key, new_Value):
        """
        Set and overwrite Android environment settings

        :: Params
        - setting_key : Specify the setting you want to change
            + android_Tools : Set the path of Android SDK tools
            + android_platform_Tools : Set the path of Android SDK platform tools (i.e. Operating System SDK)
            + android_cmdline_tools_Bin : Set the path containing the Android SDK cmdlinetools Binary files
            + DEPENDENCIES : Set list of all dependencies
            - project_primary_Language : Specify the primary langage of the project to use
                - Supported Languages
                    + java
                    + kotlin

        - new_Value : Specify the new value to overwrite
            Type: String
        """
        self.settings["android_tools_Info"][setting_key] = new_Value

    def set_project_structure(self, setting_key, new_Value):
        """
        Set and overwrite template project filesystem structure

        :: Params
        - setting_key : Specify the setting you want to change
            + application-source : Set a new project application source directory - Contains backend and frontend resource files
            + resources : Set a new application resources (res) directory
            + res-layout : Set a new layouts and Frontend Design (res/layouts) directory
            + res-drawables : Set a new Drawables (res/drawable) directory
            + res-mipmap : Set a new Mipmap Drawables (res/mipmap) directory
            + res-values : Set a new Value specification XML files (res/values) directory

        - new_Value : Specify the new value to overwrite
            Type: String
        """
        self.settings["project_Info"][setting_key] = new_Value

    def set_project_Settings(self, setting_key, new_Value):
        """
        Set and overwrite project configuration/settings

        :: Params
        - setting_key : Specify the setting you want to change
            + project_root_Dir : Set a new project root directory path
            + root_dir_Name : Set a new project root directory name
            + organization name : Set a new organization name
            + project_Name : Set a new project name
            + application_Name : Set a new application name
            + android_sdk_Packages : Specify list of all Android SDK package dependencies to download and install using sdkmanager
            + target_directories : Specify key-value (dictionary) mappings of names to the path of the target directories to create
            + target_files : Specify key-value (dictionary) mappings of names to the path of the target files to create

        - new_Value : Specify the new value to overwrite
            Type: String
        """
        self.settings["project_Info"][setting_key] = new_Value

    def update_Settings(self, setting_key, setting_subkey, new_Value):
        """
        Set and overwrite an existing project configuration/settings key and subkeys

        :: Params
        - setting_key : Specify the setting you want to change (Layer 1)
            + Type: String

        - setting_subkey : Specify the setting options you want to change (Layer 2)
            + Type: String

        - new_Value : Specify the new value to overwrite
            Type: String
        """
        self.settings[setting_subkey][setting_key] = new_Value

    def import_settings(self, settings_file_Name="settings.yaml"):
        """
        Import a custom settings file and overwrite the default 'apg.settings' contents (WIP

        :: Params
        - settings_file_Name : The file name of the configuration file containing the custom APG settings you wish to overwrite and specify
            Type: String
        """
        # Open YAML file

        # Read in YAML contents

    """
    Android project structure functions
    """
    def dl_Dependencies(self):
        """
        Download Dependencies
        """
        # Initialize Variables
        packages = ""

        # Format package list into string
        android_sdk_root_Dir = self.settings["env"]["ANDROID_HOME"]
        packages = ' '.join(self.settings["project_Info"]["android_sdk_Packages"])

        # Format command string
        cmd_str = "sdkmanager --sdk_root={} {}".format(android_sdk_root_Dir, packages)

        ## Install Android SDK packages and components
        os.system(cmd_str)

    def generate_template_Project(self):
        """
        Generate template project structure
        """
        # Initialize Variables
        cmd_str = ""
        project_root_Dir = self.settings["project_Info"]["project_root_Dir"]
        project_primary_Language = self.settings["android_tools_Info"]["project_primary_Language"]
        target_directories = self.settings["project_Info"]["target_directories"].copy()
        target_files = self.settings["project_Info"]["target_files"].copy()

        print("Project Root Dir: {}".format(project_root_Dir))
        print("Primary Language: {}".format(project_primary_Language))
        print("Target Directories: {}".format(target_directories))
        print("Target Files: {}".format(target_files))

        # Make project root directory
        os.mkdir(project_root_Dir)

        # Enter project root directory
        os.chdir(project_root_Dir)

        # Initialize Gradle
        ## Switch through language types and initialize project using gradle based on the specified language
        match project_primary_Language:
            case "java":
                cmd_str = "gradle init --type java-library"
            case "kotlin":
                cmd_str = "gradle init --type kotlin-library"
            case _:
                # Invalid language
                print("Invalid language specified: {}".format(project_primary_Language))

        print("Command String: {}".format(cmd_str))

        # Check if command string is found
        if cmd_str != "":
            os.system(cmd_str)

        # Generate template project structure
        for directories_Name, directories_Path in target_directories.items():
            # Format directory and file
            full_directory = directories_Path + self.apg_Object.file_path_separator + directories_Name

            # Make directory
            os.makedirs(directories_Path)

            # Check if directory exists
            if os.path.isdir(directories_Path):
                print("Directory [{}] created.".format(full_directory))
            else:
                print("Error creating Directory [{}].".format(full_directory))

        # Generate template project source files
        for file_Name, file_Path in target_files.items():
            # Prepare variables
            file_path_name = "{}{}{}".format(file_Path, self.apg_Object.file_path_separator, file_Name)

            try:
                # Create file
                with open(file_path_name, "a+") as write_file:
                    # Write newline to file
                    write_file.write("")

                    # Close file after usage
                    write_file.close()

                print("File [{}] created.".format(file_path_name))
            except Exception as ex:
                print("Error creating File [{}] : {}.".format(file_path_name, ex))

    def populate_template_Project(self):
        """
        Populate project source files with contents
        """

        # Initialize Variables
        project_root_Dir = self.settings["project_Info"]["project_root_Dir"]
        project_primary_Language = self.settings["android_tools_Info"]["project_primary_Language"]
        target_directories = self.settings["project_Info"]["target_directories"].copy()
        target_files = self.settings["project_Info"]["target_files"].copy()

        android_Manifest="""
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="[organization-name].[project-name].[application.name]">

    <!-- Permissions -->
    <!-- Add any permissions your app requires here -->
    <!-- Example: -->
    <uses-permission android:name="android.permission.INTERNET" />

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">

        <!-- Activities -->
        <activity android:name=".MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

        <!-- Other components -->
        <!-- Add other components like services, receivers, etc. if needed -->

    </application>

</manifest>
        """

        activity_main_Java="""
package [organization-name].[project-name].[application-name];

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        // Your code logic goes here

        TextView textView = findViewById(R.id.textView);
        textView.setText("Hello, Android!");
    }
}
        """

        activity_main_XML="""
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="16dp">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello, Android!"
        android:textSize="24sp"
        android:layout_centerInParent="true"/>
</RelativeLayout>
        """

        strings="""
<resources>
    <!-- App Name -->
    <string name="app_name">MyAndroidApp</string>

    <!-- Example Strings -->
    <string name="hello_text">Hello, Android!</string>
    <string name="welcome_message">Welcome to My Android App</string>

    <!-- Other Strings -->
    <!-- Add other strings used in your app here -->
</resources>
        """

        styles = """
<resources>

    <!-- Base application theme -->
    <style name="AppTheme" parent="Theme.AppCompat.Light.DarkActionBar">
        <!-- Customize your theme here -->
        <item name="colorPrimary">@color/colorPrimary</item> <!-- Primary branding color -->
        <item name="colorPrimaryDark">@color/colorPrimaryDark</item> <!-- Darker variant of primary color -->
        <item name="colorAccent">@color/colorAccent</item> <!-- Accent color for UI elements -->
        <!-- Other theme attributes -->

        <!-- ActionBar styles -->
        <!-- Customize ActionBar styles here -->

        <!-- App-wide text appearance -->
        <item name="android:textAppearance">@style/AppTextAppearance</item>

        <!-- Add any other customizations or overrides here -->
    </style>

    <!-- Text Appearance for the entire app -->
    <style name="AppTextAppearance" parent="TextAppearance.AppCompat">
        <!-- Customize text appearance here -->
        <item name="android:textColor">@color/textColor</item> <!-- Default text color -->
        <!-- Other text attributes -->
    </style>

</resources>
        """

        colors="""
<resources>
    <!-- Primary branding color -->
    <color name="colorPrimary">#3F51B5</color>

    <!-- Darker variant of primary color -->
    <color name="colorPrimaryDark">#303F9F</color>

    <!-- Accent color for UI elements -->
    <color name="colorAccent">#FF4081</color>

    <!-- Text color -->
    <color name="textColor">#000000</color>
    
    <!-- Additional colors -->
    <!-- <color name="secondaryColor">#2196F3</color> -->
    <!-- <color name="highlightColor">#FFC107</color> -->
    <!-- Add more colors as needed -->
</resources>
        """

        content_Mappings = {
            "AndroidManifest.xml" : android_Manifest,
            "MainActivity.java" : activity_main_Java,
            "activity_main.xml" : activity_main_XML,
            "strings.xml" : strings,
            "styles.xml" : styles,
            "colors.xml" : colors,
        }

        for target_fileName, target_file_Contents in content_Mappings.items():
            # Get content filepath
            target_filePath = target_files[target_fileName]

            # Compile filename and path
            target_File = "{}{}{}".format(target_filePath, self.apg_Object.file_path_separator, target_fileName)

            # Write content to file
            print("Writing to file: {}".format(target_File))

            try:
                with open(target_File, "a+") as write_project_Contents:
                    # Write contents to file
                    write_project_Contents.write(target_file_Contents + "\n")

                    # Close file after usage
                    write_project_Contents.close()

                print("Successfully populated {}".format(target_File))
            except Exception as ex:
                print("Error populating {} : {}".format(target_File, ex))

    def populate_build_Files(self):
        """
        Populate gradle build files with the proper project files
        """
        # Initialize Variables
        project_root_Dir = self.settings["project_Info"]["project_root_Dir"]
        project_primary_Language = self.settings["android_tools_Info"]["project_primary_Language"]
        target_directories = self.settings["project_Info"]["target_directories"].copy()
        target_files = self.settings["project_Info"]["target_files"].copy()

        gradle_build_Module = """
apply plugin: '[plugin-id]'

android {
    compileSdkVersion [android-sdk-version]
    namespace = "[organization-name].[project-name].[application-name]"
    defaultConfig {
        applicationId "organization-name.project-name.application-name"
        minSdkVersion [android-minimum-sdk-version]
        targetSdkVersion [android-target-sdk-version]
        versionCode [your-codes-current-version-number]
        versionName "your-codes-current-version-name"
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }
    buildTypes {
        release {
            // Customize your release build settings if needed
        }
    }
}

dependencies {
    implementation 'com.android.support:appcompat-v7:28.0.0'
    implementation 'com.android.support.constraint:constraint-layout:1.1.3'
    
    // Other dependencies as needed for your project
}
        """

        gradle_build_Top = """
// Top-level build file where you can add configuration options common to all sub-projects/modules.

// Declare buildscript repositories
buildscript {
    repositories {
        google() // Google's Maven repository
        jcenter() // JCenter repository
        // Add any other repositories here if needed
    }
    dependencies {
        classpath 'com.android.tools.build:gradle:[gradle-plugin-version]' // Android Gradle Plugin version
        // Add other build dependencies here if needed
    }
}

// All projects in the root project
allprojects {
    repositories {
        google() // Google's Maven repository
        jcenter() // JCenter repository
        // Add any other repositories here if needed
    }
}

// Configuration specific to the root project
task clean(type: Delete) {
    delete rootProject.buildDir
}
        """

        gradle_Settings = """
// Configure the modules included in the project

// Include the app module
include ':app'

// Include other modules if present
// For example:
// include ':library_module'

// Set the root project
rootProject.name = "your-root-application-name"
        """

        ## Top-level Gradle file
        target_fileName = "build.gradle"
        target_filePath = project_root_Dir
        target_File = "{}{}{}".format(target_filePath, self.apg_Object.file_path_separator, target_fileName)
        try:
            with open(target_File, "a+") as write_target_File:
                # Write contents
                write_target_File.write(gradle_build_Top)

                # Close file after usage
                write_target_File.close()
            print("Successfully populated {}".format(target_File))
        except Exception as ex:
            print("Error populating {} : {}".format(target_File, ex))

        ## Module-level Gradle file
        target_fileName="build.gradle"
        target_filePath="{}{}app".format(project_root_Dir, self.apg_Object.file_path_separator)
        target_File="{}{}{}".format(target_filePath, self.apg_Object.file_path_separator, target_fileName)
        try:
            with open(target_File, "a+") as write_target_File:
                # Write contents
                write_target_File.write(gradle_build_Module)

                # Close file after usage
                write_target_File.close()
            print("Successfully populated {}".format(target_File))
        except Exception as ex:
            print("Error populating {} : {}".format(target_File, ex))

        ## Gradle settings
        target_fileName="settings.gradle"
        target_filePath = project_root_Dir
        target_File="{}{}{}".format(target_filePath, self.apg_Object.file_path_separator, target_fileName)
        try:
            with open(target_File, "a+") as write_target_File:
                # Write contents
                write_target_File.write(gradle_Settings)

                # Close file after usage
                write_target_File.close()
            print("Successfully populated {}".format(target_File))
        except Exception as ex:
            print("Error populating {} : {}".format(target_File, ex))

class APGUtils():
    """
    Utilities and Functions used for APG
    """
    def join_Paths(self, delimiter, paths=None):
        """
        Join a list of paths together with a delimiter

        :: Params
        - delimiter : Specify the separator used to join the directories
            Type: String
            Delimiter Types:
                - Windows: "\\"
                - Linux: "/"

        - paths : List of paths to join
            Type: List
        """
        # Initialize Variables
        final_Path = ""

        # Check if path list is provided
        if paths != None:
            # List is not empty
            # Get size of list
            path_Size = len(paths)

            # Loop through paths
            for i in range(path_Size):
                # Get current path
                curr_Path = paths[i]

                # Concatenate path
                final_Path += curr_Path + delimiter

        # Output
        return final_Path

class APGLinux():
    """
    Contains Linux/UNIX system environment settings/configuration used by the Android Project Generator
    """
    def __init__(self):
        self.init()
        self.init_settings()
        self.reset_defaults()

    def init(self):
        """
        Initialize Variables
        """
        self.apg_utils = APGUtils()
        self.home_dir = os.environ.get("HOME")
        self.file_path_separator = "/"
        self.config_file = "{}/.bashrc".format(self.home_dir)

    def init_settings(self):
        """
        Initialize project settings
        """
        # env
        self.ANDROID_HOME = "/usr/lib/android-sdk"
        self.ANDROID_USER_HOME = "{}/.config/android".format(self.home_dir)
        self.ANDROID_EMULATOR_HOME = "{}/emulator".format(self.ANDROID_USER_HOME)
        self.ANDROID_AVD_HOME = "{}/avd".format(self.ANDROID_USER_HOME)
        self.ANDROID_SDK_COMMAND_LINE_TOOLS = "https://dl.google.com/android/repository/commandlinetools-win-10406996_latest.zip"
        self.android_sdk_Packages = [
            # Place your Android SDK packages and components here
            "platform-tools",
            "cmdline-tools;latest",
            "platforms;android-32",
            "build-tools;31.0.0",
            "system-images;android-31;google_apis;x86_64",
        ]

        # Android Tools Information
        self.android_Tools = "{}/tools".format(self.ANDROID_HOME)
        self.android_platform_Tools = "{}/platform-tools".format(self.ANDROID_HOME)
        self.android_cmdline_tools_Bin =  "{}/cmdline-tools/latest/bin".format(self.ANDROID_HOME)
        self.DEPENDENCIES =  ["android-sdk", "gradle"]
        self.project_primary_Language = "java" # Specify main backend language (java | kotlin)

        # project_Info
        self.root_dir_Name = "test-project"
        self.organization_Name = "com"
        self.project_Name = "example"
        self.application_Name = "test_app"
        self.project_root_Dir =  "{}/{}".format(os.getcwd(), self.root_dir_Name)

        # project_structure
        self.application_source = "{}/app/src/{}".format(self.project_root_Dir, "main") # Project application source directory - Contains backend and frontend resource files
        self.backend_directory = "{}/{}/{}/{}/{}".format(
            # Project application backend source files - i.e. Java/Kotlin
            self.application_source,
            self.project_primary_Language,
            self.organization_Name,
            self.project_Name,
            self.application_Name
        )
        self.resources = "{}/res".format(self.application_source) # Project Resource Files
        self.res_layout = "{}/layout".format(self.resources) # Project Resources - Layouts and Frontend Design
        self.res_drawables = "{}/drawable".format(self.resources) # Project Resources - Drawable files
        self.res_mipmap = "{}/mipmap".format(self.resources) # Project Resources - Mipmap Drawables
        self.res_values = "{}/values".format(self.resources) # Project Resources - Value specification XML files

        # Android Project Template
        self.target_directories = {
            # "directory-name" : "directory-path",
            "backend" : self.backend_directory,
            "frontend-layout" : self.res_layout,
            "frontend-drawable" : self.res_drawables,
            "frontend-mipmap" : self.res_mipmap,
            "frontend-values" : self.res_values,
        }
        self.target_files = {
            # [file-name]="file-path"
            "AndroidManifest.xml" : self.application_source,
            "MainActivity.java" : self.backend_directory,
            "activity_main.xml" : self.res_layout,
            "colors.xml" : self.res_values,
            "styles.xml" : self.res_values,
            "strings.xml" : self.res_values,
        }

    def reset_defaults(self):
        self.settings = {
            # Settings and Configurations
            "env" : {
                ## Environment Variables
                "ANDROID_HOME" : self.ANDROID_HOME,
                "ANDROID_USER_HOME" : self.ANDROID_USER_HOME,
                "ANDROID_EMULATOR_HOME" : self.ANDROID_EMULATOR_HOME,
                "ANDROID_AVD_HOME" : self.ANDROID_AVD_HOME,
            },
            "android_tools_Info" : {
                ## Custom
                "android_Tools" : self.android_Tools,
                "android_platform_Tools" : self.android_platform_Tools,
                "android_cmdline_tools_Bin" : self.android_cmdline_tools_Bin,
                "DEPENDENCIES" : self.DEPENDENCIES,
                "project_primary_Language" : self.project_primary_Language, # Specify main backend language (java | kotlin)
            },
            "project_structure" : {
                # Alias names for the project structurem folders
                "application-source" : self.application_source, # Project application source directory - Contains backend and frontend resource files
                "backend" : self.backend_directory,
                "resources" : self.resources, # Project Resource Files
                "res-layout" : self.res_layout, # Project Resources - Layouts and Frontend Design
                "res-drawables" : self.res_drawables, # Project Resources - Drawable files
                "res-mipmap" : self.res_mipmap, # Project Resources - Mipmap Drawables
                "res-values" : self.res_values, # Project Resources - Value specification XML files
            },
            "project_Info" : {
                ## Project
                "root_dir_Name"  : self.root_dir_Name,
                "organization_Name" : self.organization_Name,
                "project_Name" : self.project_Name,
                "application_Name" : self.application_Name,
                "project_root_Dir" : self.project_root_Dir,
                "ANDROID_SDK_COMMAND_LINE_TOOLS" : self.ANDROID_SDK_COMMAND_LINE_TOOLS,
                "android_sdk_Packages" : self.android_sdk_Packages.copy(),
                "target_directories" : self.target_directories.copy(),
                "target_files" : self.target_files.copy(),
            }
        }

    def setup_Env(self):
        """
        Setup Environment Variables
        """
        # Initialize Variables
        env_to_Write = [
            "ANDROID_HOME=\"{}\"".format(self.settings["env"]["ANDROID_HOME"]),
            "ANDROID_USER_HOME=\"{}\"".format(self.settings["env"]["ANDROID_USER_HOME"]),
            "ANDROID_EMULATOR_HOME={}".format(self.settings["env"]["ANDROID_EMULATOR_HOME"]),
            "ANDROID_AVD_HOME={}".format(self.settings["env"]["ANDROID_AVD_HOME"]),
            "PATH+=\"{}:{}:{}:{}:\"".format(
                self.settings["env"]["ANDROID_EMULATOR_HOME"],
                self.settings["android_tools_Info"]["android_Tools"],
                self.settings["android_tools_Info"]["android_platform_Tools"],
                self.settings["android_tools_Info"]["android_cmdline_tools_Bin"],
            ),
        ]
        config_file = "{}/.bashrc".format(self.home_dir)
        line = ""
        shell_Contents = []

        # Check if shell resource (config file) exists
        if os.path.isfile(config_file):
            # File exists
            # Read shell config file

            # Read shell resource (config) file
            with open(config_file, "r") as read_Config:
                # Go through each line

                # Read next line
                line = read_Config.readline().rstrip("\n")

                while line != "":
                    # Process line
                    # Append line into shell contents
                    shell_Contents.append(line)

                    # Read next line
                    line = read_Config.readline().rstrip("\n")

                # Close file after usage
                read_Config.close()

        # Read shell resource (config) file
        with open(config_file, "a+") as append_Config:
            # Loop through all environment variables
            for env in env_to_Write:
                # Check if environment variable in shell
                print("Checking [{}] in [{}]...".format(env, config_file))
                if not (env in shell_Contents):
                    # Is not in line
                    print("[{}] not found, writing...".format(env))
                    # Append Environment Variables and system paths into bashrc file
                    append_Config.write(env + "\n")
                else:
                    print("[{}] found.".format(env))

                print("")

            # Close file after usage
            append_Config.close()

class APGWindows():
    """
    Contains Windows system environment settings/configuration used by the Android Project Generator
    """
    def __init__(self):
        self.init()
        self.init_settings()
        self.reset_defaults()

    def init(self):
        """
        Initialize Variables
        """
        # self.home_dir = os.environ.get("HOMEDIR")
        # self.cwd = os.environ.get("CD")
        self.apg_utils = APGUtils()
        self.home_dir = os.getcwd()
        self.cwd = os.getcwd()
        self.file_path_separator = "\\"
        self.env_filename = "apg-shell.bat"
        self.env_config_file_fullpath = r"{}\{}".format(os.getcwd(), self.env_filename)

    def init_settings(self):
        """
        Initialize project settings
        """
        # env
        self.ANDROID_HOME = "{}\\android-sdk".format(self.cwd)
        self.ANDROID_USER_HOME = "{}\\.config\\android".format(self.home_dir)
        self.ANDROID_EMULATOR_HOME = "{}\\emulator".format(self.ANDROID_USER_HOME)
        self.ANDROID_AVD_HOME = "{}\\avd".format(self.ANDROID_USER_HOME)
        self.ANDROID_SDK_COMMAND_LINE_TOOLS = "https://dl.google.com/android/repository/commandlinetools-win-10406996_latest.zip"
        self.android_sdk_Packages = [
            # Place your Android SDK packages and components here
            "platform-tools",
            "cmdline-tools;latest",
            "platforms;android-32",
            "build-tools;31.0.0",
            "system-images;android-31;google_apis;x86_64",
        ]

        # Android Tools Information
        self.android_Tools = "{}\\tools".format(self.ANDROID_HOME)
        self.android_platform_Tools = "{}\\platform-tools".format(self.ANDROID_HOME)
        self.android_cmdline_tools_Bin =  "{}\\cmdline-tools\\latest\\bin".format(self.ANDROID_HOME)
        self.DEPENDENCIES =  ["android-sdk", "gradle"]
        self.project_primary_Language = "java" # Specify main backend language (java | kotlin)

        # project_Info
        self.root_dir_Name = "test-project"
        self.organization_Name = "com"
        self.project_Name = "example"
        self.application_Name = "test_app"
        self.project_root_Dir =  "{}\\{}".format(os.getcwd(), self.root_dir_Name)

        # project_structure
        self.application_source = "{}\\app\\src\\{}".format(self.project_root_Dir, "main") # Project application source directory - Contains backend and frontend resource files
        self.backend_directory = "{}\\{}\\{}\\{}\\{}".format(
            # Project application backend source files - i.e. Java/Kotlin
            self.application_source,
            self.project_primary_Language,
            self.organization_Name,
            self.project_Name,
            self.application_Name
        )
        self.resources = "{}\\res".format(self.application_source) # Project Resource Files
        self.res_layout = "{}\\layout".format(self.resources) # Project Resources - Layouts and Frontend Design
        self.res_drawables = "{}\\drawable".format(self.resources) # Project Resources - Drawable files
        self.res_mipmap = "{}\\mipmap".format(self.resources) # Project Resources - Mipmap Drawables
        self.res_values = "{}\\values".format(self.resources) # Project Resources - Value specification XML files

        # Android Project Template
        self.target_directories = {
            # "directory-name" : "directory-path",
            "backend" : self.backend_directory,
            "frontend-layout" : self.res_layout,
            "frontend-drawable" : self.res_drawables,
            "frontend-mipmap" : self.res_mipmap,
            "frontend-values" : self.res_values,
        }
        self.target_files = {
            # [file-name]="file-path"
            "AndroidManifest.xml" : self.application_source,
            "MainActivity.java" : self.backend_directory,
            "activity_main.xml" : self.res_layout,
            "colors.xml" : self.res_values,
            "styles.xml" : self.res_values,
            "strings.xml" : self.res_values,
        }

    def reset_defaults(self):
        self.settings = {
            # Settings and Configurations
            "env" : {
                ## Environment Variables
                "ANDROID_HOME" : self.ANDROID_HOME,
                "ANDROID_USER_HOME" : self.ANDROID_USER_HOME,
                "ANDROID_EMULATOR_HOME" : self.ANDROID_EMULATOR_HOME,
                "ANDROID_AVD_HOME" : self.ANDROID_AVD_HOME,
            },
            "android_tools_Info" : {
                ## Custom
                "android_Tools" : self.android_Tools,
                "android_platform_Tools" : self.android_platform_Tools,
                "android_cmdline_tools_Bin" : self.android_cmdline_tools_Bin,
                "DEPENDENCIES" : self.DEPENDENCIES,
                "project_primary_Language" : self.project_primary_Language, # Specify main backend language (java | kotlin)
            },
            "project_structure" : {
                # Alias names for the project structurem folders
                "application-source" : self.application_source, # Project application source directory - Contains backend and frontend resource files
                "backend" : self.backend_directory,
                "resources" : self.resources, # Project Resource Files
                "res-layout" : self.res_layout, # Project Resources - Layouts and Frontend Design
                "res-drawables" : self.res_drawables, # Project Resources - Drawable files
                "res-mipmap" : self.res_mipmap, # Project Resources - Mipmap Drawables
                "res-values" : self.res_values, # Project Resources - Value specification XML files
            },
            "project_Info" : {
                ## Project
                "root_dir_Name"  : self.root_dir_Name,
                "organization_Name" : self.organization_Name,
                "project_Name" : self.project_Name,
                "application_Name" : self.application_Name,
                "project_root_Dir" : self.project_root_Dir,
                "ANDROID_SDK_COMMAND_LINE_TOOLS" : self.ANDROID_SDK_COMMAND_LINE_TOOLS,
                "android_sdk_Packages" : self.android_sdk_Packages.copy(),
                "target_directories" : self.target_directories.copy(),
                "target_files" : self.target_files.copy(),
            }
        }

    def setup_Env(self):
        """
        Setup Environment Variables
        """
        # Initialize Variables
        env_to_Write = [
            "SET ANDROID_HOME=\"{}\"".format(self.settings["env"]["ANDROID_HOME"]),
            "SET ANDROID_USER_HOME=\"{}\"".format(self.settings["env"]["ANDROID_USER_HOME"]),
            "SET ANDROID_EMULATOR_HOME={}".format(self.settings["env"]["ANDROID_EMULATOR_HOME"]),
            "SET ANDROID_AVD_HOME={}".format(self.settings["env"]["ANDROID_AVD_HOME"]),
            "SET PATH=\"%PATH%;{};{};{};{};\"".format(
                self.settings["env"]["ANDROID_EMULATOR_HOME"],
                self.settings["android_tools_Info"]["android_Tools"],
                self.settings["android_tools_Info"]["android_platform_Tools"],
                self.settings["android_tools_Info"]["android_cmdline_tools_Bin"],
            ),
        ]
        env_filename = self.env_filename
        config_file = self.env_config_file_fullpath
        line = ""
        shell_Contents = []

        # Check if shell resource (config file) exists
        if os.path.isfile(config_file):
            # File exists
            # Read shell config file
            with open(config_file, "r") as read_Config:
                # Go through each line

                # Read next line
                line = read_Config.readline().rstrip("\n")

                while line != "":
                    # Process line
                    # Append line into shell contents
                    shell_Contents.append(line)

                    # Read next line
                    line = read_Config.readline().rstrip("\n")

                # Close file after usage
                read_Config.close()

        # Open shell resource (config) file to write
        with open(config_file, "a+") as append_Config:
            # Loop through all environment variables
            for env in env_to_Write:
                # Check if environment variable in shell
                print("Checking [{}] in [{}]...".format(env, config_file))
                if not (env in shell_Contents):
                    # Is not in line
                    print("[{}] not found, writing...".format(env))
                    # Append Environment Variables and system paths into bashrc file
                    append_Config.write(env + "\n")
                else:
                    print("[{}] found.".format(env))

                print("")

            # Close file after usage
            append_Config.close()


