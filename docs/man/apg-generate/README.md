# apg-generate : Android Project Generator - Generate-focused

## Information
### Description
+ apg - The Android Project Generator - is a project/package workspace generator CLI utility for generating a working Android application development workspace that can be edited and built OOTB

### Notes
+ Please refer to the main repository that holds this script [Thanatisia/android-project-generator python](https://github.com/Thanatisia/android-project-generator/tree/main/app/languages/python) for the latest updates
+ Currently apg's environment variables setup is supporting only Windows, Linux is in the pipeline

## Setup
### Dependencies
- android-sdk
    + cmdline-tools
+ gradle

### Pre-Requisites
- Set environment variables in your shell
    - Linux
        + `ANDROID_HOME="/path/to/android-sdk"`
        + `ANDROID_USER_HOME="/path/to/user/home/.config/android"`
        + `ANDROID_EMULATOR_HOME="[ANDROID_USER_HOME]/emulator"`
        + `ANDROID_AVD_HOME="[ANDROID_USER_HOME]/avd"`
        + `PATH+="[ANDROID_EMULATOR_HOME]:[ANDROID_HOME]/tools:[ANDROID_HOME]/platform-tools:[ANDROID_HOME]/cmdline-tools/latest/bin:"`
    - Windows
        + `SET ANDROID_HOME="\path\to\android\sdk\root"`
        + `SET ANDROID_USER_HOME="\path\to\user\home\.config\android"`
        + `SET ANDROID_EMULATOR_HOME="[ANDROID_USER_HOME]\emulator"`
        + `SET ANDROID_AVD_HOME="[ANDROID_USER_HOME]\avd"`
        + `SET PATH="%PATH%;[ANDROID_EMULATOR_HOME];[ANDROID_HOME]\tools;[ANDROID_HOME]\platform-tools;[ANDROID_HOME]\cmdline-tools\latest\bin;"`

## Documentations

### Synopsis/Syntax
- Standard
    ```bash
    apg-generate {options} <arguments>
    ```

### Parameters
- Positionals
    - Actions
        - `download [type]` : Download the specified category/type
            - Items
                + dependencies : Download specified Android SDK dependencies and package libraries required for setting up a working Android application development environment workspace from scratch
        - setup : Prepare and setup the user's system environment with environment variables required for setting up a working Android application development environment workspace from scratch. 
            - Notes
                + This function is currently only supporting Windows, Linux is a WIP
        - template : Generate and populate a working Mobile application template project that you can use right Out-of-the-Box (OOTB)
            - Notes
                - The generated template project structure have certain sections populated by keywords that have to be edited by the user
                    + This is for user design
                + Hence, before building, please look through the project structure and edit according to your needs
        - gradle : Populate and setup the gradle build files within the generated template project structure; To be used after 'template'

- Optionals
    - With Arguments

    - Flags
        + `-h | --help` : Display help message
        + `-s | --view-settings` : Display current settings for system
        + `-v | --version` : Display system version information

### Usage
- Display help
    ```bash
    apg-generate --help
    ```

- Complete setup
    ```bash
    apg-generate download dependencies setup template gradle
    ```

## TODO
+ Optional argument customizations in the form of flags
+ Add Linux support for the adding of Android Environment Variables into the shell rc files

## Resources

## References

## Remarks

