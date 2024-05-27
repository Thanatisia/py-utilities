# apg : Android Project Generator

## Information

### Module
+ Type: Library/module

### Description
+ Library containing various core Android Project Generator-related objects to assist in the generating of a working, Out-of-the-Box (OOTB), Mobile (Android) Application Development Environment project and workspace

## Documentations

### Packages
- pyutils.libraries

### Modules
- pyutils.libraries
    - `.apg`

### Classes
- pyutils.libraries.apg
    - `.AndroidProjectGenerator(apg_Object)` : The primary Android Project Generator class initializer containing the core functionalities of the apg project after obntaining the platform information from the `APG[Operating System]` classes
        - Parameter Signature/Headers
            - apg_Object : Pass the `APG[Operating System]` class object instance for 'AndroidProjectGenerator()' to use
                + Type: `class<APG[Operating System]>`
        - Return
            - apg : Return the initialized AndroidProjectGenerator() class object
                + Type: `class<AndroidProjectGenerator()>`
    - `.APGLinux()` : Android Project Generator class containing Linux-based logic and functionalities for AndroidProjectGenerator to know what platform the host system is using
        - Return
            - apg_linux : Return the initialized APGLinux() class object
                + Type: `class<APGLinux()>`
    - `.APGWindows()` : Android Project Generator class containing Windows-based logic and functionalities for AndroidProjectGenerator to know what platform the host system is using
        - Return
            - apg_win : Return the initialized APGWindows() class object
                + Type: `class<APGWindows()>`
    - `.APGUtils()` : Android Project Generator utilities class containing various generic Android project utilities and functionalities
        - Return
            - apg_utils : Return the initialized APGUtils() class object
                + Type: `class<APGUtils()>`

### Data Types/Objects

### Functions
- pyutils.libraries.apg.AndroidProjectGenerator()
    - System Environment Functions
        - `.set_android_Environment(setting_key, new_Value)`: Set and overwrite Android environment settings
            - Parameter Signature/Headers
                - setting_key : Specify the setting you want to change
                    + Type: String
                    - Setting Keys
                        + ANDROID_HOME : Set the Android SDK root directory
                        + ANDROID_USER_HOME : Set the Android SDK user home directory
                        + ANDROID_EMULATOR_HOME : Set the home path of the Android SDK official Emulator
                        + ANDROID_AVD_HOME : Set the home path of the Android SDK Virtual Device

                - new_Value : Specify the new value to overwrite
                    + Type: String
            + Format: `self.settings["env"][setting_key] = new_Value`

        - `.set_android_Tools(setting_key, new_Value)`: Set and overwrite Android environment settings
            - Parameter Signature/Headers
                - setting_key : Specify the setting you want to change
                    + Type: String
                    - Keywords
                        + android_Tools : Set the path of Android SDK tools
                        + android_platform_Tools : Set the path of Android SDK platform tools (i.e. Operating System SDK)
                        + android_cmdline_tools_Bin : Set the path containing the Android SDK cmdlinetools Binary files
                        + DEPENDENCIES : Set list of all dependencies
                        - project_primary_Language : Specify the primary langage of the project to use
                            - Supported Languages
                                + java
                                + kotlin

                - new_Value : Specify the new value to overwrite
                    + Type: String
            + Format: `self.settings["android_tools_Info"][setting_key] = new_Value`

        - `.set_project_structure(setting_key, new_Value)`: Set and overwrite template project filesystem structure
            - Parameter Signature/Headers
                - setting_key : Specify the setting you want to change
                    + Type: String
                    - Setting Keys
                        + application-source : Set a new project application source directory - Contains backend and frontend resource files
                        + resources : Set a new application resources (res) directory
                        + res-layout : Set a new layouts and Frontend Design (res/layouts) directory
                        + res-drawables : Set a new Drawables (res/drawable) directory
                        + res-mipmap : Set a new Mipmap Drawables (res/mipmap) directory
                        + res-values : Set a new Value specification XML files (res/values) directory

                - new_Value : Specify the new value to overwrite
                    + Type: String
            + Format: `self.settings["project_Info"][setting_key] = new_Value`

        - `.set_project_Settings(setting_key, new_Value)`: Set and overwrite project configuration/settings
            - Parameter Signature/Headers
                - setting_key : Specify the setting you want to change
                    + Type: String
                    - Setting Keywords
                        + project_root_Dir : Set a new project root directory path
                        + root_dir_Name : Set a new project root directory name
                        + organization name : Set a new organization name
                        + project_Name : Set a new project name
                        + application_Name : Set a new application name
                        + android_sdk_Packages : Specify list of all Android SDK package dependencies to download and install using sdkmanager
                        + target_directories : Specify key-value (dictionary) mappings of names to the path of the target directories to create
                        + target_files : Specify key-value (dictionary) mappings of names to the path of the target files to create

                - new_Value : Specify the new value to overwrite
                    + Type: String
            + Format: `self.settings["project_Info"][setting_key] = new_Value`

        - `.update_Settings(setting_key, setting_subkey, new_Value)`: Set and overwrite an existing project configuration/settings key and subkeys
            - Parameter Signature/Headers
                - setting_key : Specify the setting you want to change (Layer 1)
                    + Type: String

                - setting_subkey : Specify the setting options you want to change (Layer 2)
                    + Type: String

                - new_Value : Specify the new value to overwrite
                    + Type: String
            + Format: `self.settings[setting_subkey][setting_key] = new_Value`

        - `.import_settings(settings_file_Name="settings.yaml")`: Import a custom settings file and overwrite the default 'apg.settings' contents (WIP)
            - Parameter Signature/Headers
                - settings_file_Name : The file name of the configuration file containing the custom APG settings you wish to overwrite and specify
                    + Type: String
                    + Default: "settings.yaml"

    - Android project structure functions
        + `.dl_Dependencies()`: Download Android SDK Dependencies and packages from sdkmanager to ANDROID_HOME
        + `.generate_template_Project()`: Generate a working Android template project workspace out-of-the-box, ready for developer to edit and compile
        + `.populate_template_Project()`: Populate the generated project template workspace with the Android project files
        + `.populate_build_Files()`: Populate the generated project workspace with files for the gradle build system

- pyutils.libraries.apg.APGUtils()
    - `.join_Paths(delimiter, paths=None)`: Join a list of paths together with a delimiter
        - Parameter Signature/Headers
            - delimiter : Specify the separator used to join the directories
                + Type: String
                - Delimiter Types:
                    + Windows: "\\"
                    + Linux: "/"

            - paths : List of paths to join
                + Type: List
        - Return
            - final_Path : Return the resulting path after joining a list of paths together with a delimiter/separator
                + Type: String

- pyutils.libraries.apg.APGLinux()
    + `.init()`: Perform general Pre-Initialization setup
    + `.init_settings()`: Initialize project settings
    + `.reset_defaults()`: Reset/Set default class values
    + `setup_Env()`: Setup Environment Variables to the shell configuration files

- pyutils.libraries.apg.APGWindows()
    + `.init()`: Perform general Pre-Initialization setup
    + `.init_settings()`: Initialize project settings
    + `.reset_defaults()`: Reset/Set default class values
    + `setup_Env()`: Setup Environment Variables to the shell configuration files

### Attributes/Variables
- pyutils.libraries.apg.AndroidProjectGenerator()
    - `.apg_Object` : Contains the `APG[Operating System]` class object instance
        + Type: `APG[Operating-System]`
    - `.settings`   : Contains the settings from the `APG[Operating System]` class object
        + Type: Dictionary
    - `.apg_Utils`  : Contains the initialized `APGUtils()` class object instance
        + Type: `APGUtils()`

- pyutils.libraries.apg.APGLinux()
    - Initialization
        - `.apg_utils` : Contains the initialized `APGUtils() class object instance
            + Type: `APGUtils()`
        - `.home_dir` : Contains the HOME environment variable
            + Type: String
            + Value: os.environ.get("HOME")
        - `.file_path_separator` : Specify the default filepath separator/delimiter for APGLinux (Linux systems)
            + Type: String
            + Value: "/"
        - `.config_file` : Specify the path of the user's default shell RC configuration file
            + Type: String
        - `.settings` : Specify the Linux settings for APG
            + Type: Dictionary
            - Dictionary Key-Values
            - Default Values:
                ```python
                {
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
                ```
    - Environment Variables
        - `.ANDROID_HOME` : Specify the Android SDK root directory
            + Type: String
            + Default Value: "/usr/lib/android-sdk"
        - `.ANDROID_USER_HOME`: Specify the user Android configuration directory
            + Type: String
            + Default Value: "{}/.config/android".format(self.home_dir)
        - `.ANDROID_EMULATOR_HOME` : Specify the Android Emulator configuration and data root directory
            + Type: String
            + Default Value: "{}/emulator".format(self.ANDROID_USER_HOME)
        - `.ANDROID_AVD_HOME` : Specify the user's Android Virtual Device (AVD) configuration and data root directory
            + Type: String
            + Default Value: "{}/avd".format(self.ANDROID_USER_HOME)
        - `.ANDROID_SDK_COMMAND_LINE_TOOLS` : Specify the path/URL to the Android cmdlinetools (Command Line Tools) repository
            + Type: String
            + Default Value: "https://dl.google.com/android/repository/commandlinetools-win-10406996_latest.zip"
        - `.android_sdk_Packages` : Provide a list of all Android SDK dependencies and packages to install using sdkmanager
            + Type: List
            - Default Value: 
                ```python
                [
                    # Place your Android SDK packages and components here
                    "platform-tools",
                    "cmdline-tools;latest",
                    "platforms;android-32",
                    "build-tools;31.0.0",
                    "system-images;android-31;google_apis;x86_64",
                ]
                ```
    - Android Tools Information
        - `.android_Tools` : Specify the user's Android SDK Tools configuration and data root directory
            + Type: String
            + Default Values: "{}/tools".format(self.ANDROID_HOME)
        - `.android_platform_Tools` : Specify the user's Android SDK Platform Tools configuration and data root directory
            + Type: String
            + Default Value: "{}/platform-tools".format(self.ANDROID_HOME)
        - `.android_cmdline_tools_Bin` : Specify the cmdline tools binary directory path
            + Type: String
            + Default Value: "{}/cmdline-tools/latest/bin".format(self.ANDROID_HOME)
        - `.DEPENDENCIES` : Specify all system package dependencies required for a working Mobile (Android) Application Development Development Environment
            + Type: List 
            + Default: Values
                ```python
                ["android-sdk", "gradle"]
                ```
        - `.project_primary_Language` : Specify main backend language (java | kotlin)
            + Type: String 
            + Default Value: "java"
            - Possible Values
                + java : Generate a Java-based template project workspace
                + kotlin : Generate a Kotlin-based template project workspace

    - project_Info
        - `.root_dir_Name` : Specify the name of the project workspace's root directory
            + Type: String
            + Default Value: "test-project"
        - `.organization_Name` : Specify the organization/company domain of the project/application
            + Type: String
            + Default Value: "com"
        - `.project_Name` : Specify the project workspace's name
            + Type: String
            + Default Value: "example"
        - `.application_Name` : Specify the name of the current/new application of the new project
            + Type: String
            + Default Value: "test_app"
        - `.project_root_Dir` : Specify the path to the project workspace's root directory
            + Type: String
            + Default Value: "{}/{}".format(os.getcwd(), self.root_dir_Name)

    - project_structure
        - `.application_source` : Project application source directory - Contains backend and frontend resource files
            + Type: String
            - Default Value: "[project-root-directory]/app/src/main"
                - Notes
                    + main : This refers to the branch directory 'main' containing the main/core application source code and logic
        - `.backend_directory` : Specify the directory containing the application's Java/Kotlin source files
            + Type: String
            - Default Values: 
                ```python
                "{}/{}/{}/{}/{}".format(
                    # 
                    self.application_source,
                    self.project_primary_Language,
                    self.organization_Name,
                    self.project_Name,
                    self.application_Name
                )
                ```
        - `.resources` : Specify the Project Resource Files
            + Type: String
            + Default Values: `"{}/res".format(self.application_source)`
        - `.res_layout` : Project Resources - Layouts and Frontend Design
            + Type: String
            + Default Values: `"{}/layout".format(self.resources)`
        - `.res_drawables` : Project Resources - Drawable files
            + Type: String
            + Default Values: `"{}/drawable".format(self.resources)`
        - `.res_mipmap` : Project Resources - Mipmap Drawables
            + Type: String
            + Default Values: `"{}/mipmap".format(self.resources)`
        - `.res_values` : Project Resources - Value specification XML files
            + Type: String
            + Default Values: `"{}/values".format(self.resources)`

    - Android Project Template
        - `.target_directories` : Specify a dictionary containing a mapping of the name to the path of the directories you want to create in the project template workspace
            + Type: Dictionary (Key-Value Mappings)
            - Default Values
                ```python 
                {
                    # "directory-name" : "directory-path",
                    "backend" : self.backend_directory,
                    "frontend-layout" : self.res_layout,
                    "frontend-drawable" : self.res_drawables,
                    "frontend-mipmap" : self.res_mipmap,
                    "frontend-values" : self.res_values,
                }
                ```
        - `.target_files` : : Specify a dictionary containing a mapping of the name to the path of the files you want to create in the project template workspace
            + Type: Dictionary (Key-Value Mappings)
            - Default Values 
                ```python
                {
                    # [file-name]="file-path"
                    "AndroidManifest.xml" : self.application_source,
                    "MainActivity.java" : self.backend_directory,
                    "activity_main.xml" : self.res_layout,
                    "colors.xml" : self.res_values,
                    "styles.xml" : self.res_values,
                    "strings.xml" : self.res_values,
                }
                ```

- pyutils.libraries.apg.APGWindows()
    - Initialization
        - `.apg_utils` : Contains the initialized `APGUtils() class object instance
            + Type: `APGUtils()`
        - `.home_dir` : Contains the home directory (TODO: change to the HOME environment variable)
            + Type: String
            + Default Values: `os.getcwd()`
        - `.cwd` : Set the current working directory 
            + Type: String
            + Default Value: `os.getcwd()`
        - `.file_path_separator` : Specify the default filepath separator/delimiter for APGWindows (Windows systems)
            + Type: String
            + Value: "\\"
        - `.env_filename` : Specify the file name of the custom APG shell used for adding the System Environment Variables required for a working Android application development environment
            + Type: String
            + Default Vallue: "apg-shell.bat"
        - `.env_config_file_fullpath` : Specify the path of the user's default shell RC configuration file
            + Type: String
            + Default Value: `r"{}\{}".format(os.getcwd(), self.env_filename)`
        - `.settings` : Specify the Windows settings for APG
            + Type: Dictionary
            - Dictionary Key-Values
            - Default Values:
                ```python
                {
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
                ```
    - Environment Variables
        - `.ANDROID_HOME` : Specify the Android SDK root directory
            + Type: String
            + Default Value: "self.cwd\\android-sdk"
        - `.ANDROID_USER_HOME`: Specify the user Android configuration directory
            + Type: String
            + Default Value: "{}\\.config\\android".format(self.home_dir)
        - `.ANDROID_EMULATOR_HOME` : Specify the Android Emulator configuration and data root directory
            + Type: String
            + Default Value: "{}\\emulator".format(self.ANDROID_USER_HOME)
        - `.ANDROID_AVD_HOME` : Specify the user's Android Virtual Device (AVD) configuration and data root directory
            + Type: String
            + Default Value: "{}\\avd".format(self.ANDROID_USER_HOME)
        - `.ANDROID_SDK_COMMAND_LINE_TOOLS` : Specify the path/URL to the Android cmdlinetools (Command Line Tools) repository
            + Type: String
            + Default Value: "https://dl.google.com/android/repository/commandlinetools-win-10406996_latest.zip"
        - `.android_sdk_Packages` : Provide a list of all Android SDK dependencies and packages to install using sdkmanager
            + Type: List
            - Default Value: 
                ```python
                [
                    # Place your Android SDK packages and components here
                    "platform-tools",
                    "cmdline-tools;latest",
                    "platforms;android-32",
                    "build-tools;31.0.0",
                    "system-images;android-31;google_apis;x86_64",
                ]
                ```
    - Android Tools Information
        - `.android_Tools` : Specify the user's Android SDK Tools configuration and data root directory
            + Type: String
            + Default Values: "{}\\tools".format(self.ANDROID_HOME)
        - `.android_platform_Tools` : Specify the user's Android SDK Platform Tools configuration and data root directory
            + Type: String
            + Default Value: "{}\\platform-tools".format(self.ANDROID_HOME)
        - `.android_cmdline_tools_Bin` : Specify the cmdline tools binary directory path
            + Type: String
            + Default Value: "{}\\cmdline-tools\\latest\\bin".format(self.ANDROID_HOME)
        - `.DEPENDENCIES` : Specify all system package dependencies required for a working Mobile (Android) Application Development Development Environment
            + Type: List 
            + Default: Values
                ```python
                ["android-sdk", "gradle"]
                ```
        - `.project_primary_Language` : Specify main backend language (java | kotlin)
            + Type: String 
            + Default Value: "java"
            - Possible Values
                + java : Generate a Java-based template project workspace
                + kotlin : Generate a Kotlin-based template project workspace
    - project_Info
        - `.root_dir_Name` : Specify the name of the project workspace's root directory
            + Type: String
            + Default Value: "test-project"
        - `.organization_Name` : Specify the organization/company domain of the project/application
            + Type: String
            + Default Value: "com"
        - `.project_Name` : Specify the project workspace's name
            + Type: String
            + Default Value: "example"
        - `.application_Name` : Specify the name of the current/new application of the new project
            + Type: String
            + Default Value: "test_app"
        - `.project_root_Dir` : Specify the path to the project workspace's root directory
            + Type: String
            + Default Value: "{}\\{}".format(os.getcwd(), self.root_dir_Name)
    - project_structure
        - `.application_source` : Project application source directory - Contains backend and frontend resource files
            + Type: String
            - Default Value: "[project-root-directory]\\app\\src\\main"
                - Notes
                    + main : This refers to the branch directory 'main' containing the main/core application source code and logic
        - `.backend_directory` : Specify the directory containing the application's Java/Kotlin source files
            + Type: String
            - Default Values: 
                ```python
                "{}\\{}\\{}\\{}\\{}".format(
                    # 
                    self.application_source,
                    self.project_primary_Language,
                    self.organization_Name,
                    self.project_Name,
                    self.application_Name
                )
                ```
        - `.resources` : Specify the Project Resource Files
            + Type: String
            + Default Values: `"{}\\res".format(self.application_source)`
        - `.res_layout` : Project Resources - Layouts and Frontend Design
            + Type: String
            + Default Values: `"{}\\layout".format(self.resources)`
        - `.res_drawables` : Project Resources - Drawable files
            + Type: String
            + Default Values: `"{}\\drawable".format(self.resources)`
        - `.res_mipmap` : Project Resources - Mipmap Drawables
            + Type: String
            + Default Values: `"{}\\mipmap".format(self.resources)`
        - `.res_values` : Project Resources - Value specification XML files
            + Type: String
            + Default Values: `"{}\\values".format(self.resources)`
    - Android Project Template
        - `.target_directories` : Specify a dictionary containing a mapping of the name to the path of the directories you want to create in the project template workspace
            + Type: Dictionary (Key-Value Mappings)
            - Default Values
                ```python 
                {
                    # "directory-name" : "directory-path",
                    "backend" : self.backend_directory,
                    "frontend-layout" : self.res_layout,
                    "frontend-drawable" : self.res_drawables,
                    "frontend-mipmap" : self.res_mipmap,
                    "frontend-values" : self.res_values,
                }
                ```
        - `.target_files` : : Specify a dictionary containing a mapping of the name to the path of the files you want to create in the project template workspace
            + Type: Dictionary (Key-Value Mappings)
            - Default Values 
                ```python
                {
                    # [file-name]="file-path"
                    "AndroidManifest.xml" : self.application_source,
                    "MainActivity.java" : self.backend_directory,
                    "activity_main.xml" : self.res_layout,
                    "colors.xml" : self.res_values,
                    "styles.xml" : self.res_values,
                    "strings.xml" : self.res_values,
                }
                ```

### Usage
- Simple Android project file structure
    ```python
    import os
    import sys
    from pyutils.libraries import apg

    def main():
        # To initialize for a Windows environment
        apgEnv = apg.APGWindows()

        # To initialize for a Linux environment
        apgEnv = apg.APGLinux()

        # To initialize the Generator
        apgGen = apg.AndroidProjectGenerator()

        # To setup environment
        apgEnv.setup_Env()
        
        # To download dependencies
        apgGen.dl_Dependencies()

        ## Generate template project structure
        apgGen.generate_template_Project()

        ## Populate project source files
        apgGen.populate_template_Project()

        # Create gradle files
        apgGen.populate_build_Files()

    if __name__ == "__main__":
        main()
    ```

## Wiki

## Resources

## References

## Remarks

