import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Controls.Universal 2.3
import QtQuick.Layouts 1.3
import QtQuick.Dialogs 1.3
import "components" as Comp

ApplicationWindow {
    id: mainWindow
    visible: true
    width: 800
    height: 500

    title: qsTr("Welcome | Peter Setup")
    color: "darkgrey"

    Universal.theme: Universal.Dark

    property QtObject connector
    property string license_text: ""

    property QtObject stack
    property string message: qsTr("Log Info")
    property string cont_func
    property int stage: 0

    signal updatePercent(int percent)
    signal updateMessage(string message)

    signal exit_app()
    signal rollback()
    signal showPrompt(string affirm_func, string message)

    signal declineLicensing()
    signal acceptLincense()

    signal useDefaultLocation()
    signal declineLocation()
    signal proceedAfterLocation()

    signal startServerInstallation()
    signal stopServerInstallation()
    signal proceedAfterServerInstallation()

    signal rejectAuthentication()
    signal proceedAfterAuth()

    signal startMySqlInstallation()
    signal stopMySqlInstallation()
    signal proceedAfterMySqlInstallation()

    signal startPhpInstallation()
    signal stopPhpInstallation()
    signal proceedAfterPhpInstallation()

    signal finalise()
    signal rejectFinalising()
    signal proceedAfterFinalising()

    signal closeSetup()
    signal launchApplication()


    onUpdatePercent: {
        stack.currentItem.progress_percent = percent
    }

    onUpdateMessage: {
        stack.currentItem.message = message
    }

    onExit_app: {
        if(stage == 1) {
            mainWindow.close()
        } else {
        }
    }

    onRollback: {
        Connector.rollback(stage)

        mainWindow.close()
    }

    onShowPrompt: {
        // prompt shows
        // calls the exit func
        // returns to already running code

        prompt_message.text = message
        cont_func = affirm_func
        prompt.open()

    }

    onDeclineLicensing: {
        showPrompt("exit", 'Are you sure you want to quit Setup')
    }
    onAcceptLincense:  {
        stack.push(locationComp);
    }

    onUseDefaultLocation: {
        connector.use_default_path()
    }
    onDeclineLocation: {
        // go back
        stack.pop()
    }
    onProceedAfterLocation: {
        connector.save_location(stack.currentItem.location.text)
        stack.push(serverComp);
    }

    onStartServerInstallation: {
        connector.start_server_install()
    }
    onStopServerInstallation: {
        showPrompt("rollback", "Are you sure you want to quit installation")
    }
    onProceedAfterServerInstallation: {
        stack.currentItem.done = true;
        stack.push(authComp);
    }

    onRejectAuthentication: {
        stack.pop()
    }
    onProceedAfterAuth: {
        // Authenticate
        // push next
        if(stack.currentItem.field1.text === "") {
            showPrompt('', 'Password Field cannot be empty')
        } else if(stack.currentItem.field1.text === stack.currentItem.field2.text) {
            connector.save_auth(stack.currentItem.field1.text)
            stack.push(mysqlComp);
        } else {
            // report error
            // password mismatch
            showPrompt('', 'Password does not match. Please try again')
        }
    }

    onStartMySqlInstallation: {
        connector.start_mysql_install()
    }
    onStopMySqlInstallation: {
        showPrompt("rollback", 'Are you sure you want to quit installation')
    }
    onProceedAfterMySqlInstallation: {
        stack.currentItem.done = true;
        stack.push(phpComp);
    }

    onStartPhpInstallation: {
        connector.start_php_install()
    }
    onStopPhpInstallation: {
        showPrompt("rollback", "Are you sure you want to quit")
    }
    onProceedAfterPhpInstallation: {
        stack.currentItem.done = true;
        stack.push(finalComp);
    }

    onFinalise: {
        connector.start_finalising()
    }
    onRejectFinalising: {
        showPrompt("rollback", "Are you sure you want to quit")
    }
    onProceedAfterFinalising: {
        stack.currentItem.done = true;
        swipe.currentIndex = 1
    }

    onCloseSetup: {
        mainWindow.close()
    }
    onLaunchApplication: {
        connector.launch_application()
    }

    Comp.Welcome {id: welcomeComp}
    Comp.Location {id: locationComp}
    Comp.Server {id: serverComp}
    Comp.Authenticate {id: authComp}
    Comp.MySql {id: mysqlComp}
    Comp.Php {id: phpComp}
    Comp.Finalising {id: finalComp}

    SwipeView {
        id: swipe
        anchors.fill: parent
        currentIndex: 0
        interactive: false

        Comp.Start {}

        Comp.Appreciation {}

    }

    Popup {
        id: prompt
        x: (mainWindow.width - width) / 2
        y: (mainWindow.height - height) / 2
        width: 280
        height: 280
        modal: false
        focus: true
        closePolicy: Popup.NoAutoClose

        ColumnLayout {
            anchors.fill: parent
            anchors.margins: 8

            Text {
                id: prompt_message
                Layout.fillWidth: true
                horizontalAlignment: Text.AlignHCenter
                font.family: "Segoe UI Semilight"
                wrapMode: Text.WordWrap
                font.pixelSize: 14
                text: ""
                color: "white"
                clip: true
            }

            DialogButtonBox {
                Layout.alignment: Qt.AlignBottom
                standardButtons: Dialog.Ok | Dialog.Cancel

                onAccepted: {
                    if (cont_func == 'exit') {
                        exit_app()
                        return
                    } else if (cont_func == 'rollback') {
                        rollback()
                        return
                    }
                    prompt.close()
                    return
                }
                onRejected: prompt.close()

            }
        }

    }

    FileDialog {
        id: folder_picker
        title: qsTr("Choose a Path")
        folder: shortcuts.home
        selectFolder: true

        onAccepted: {
            var url = folder_picker.fileUrl.toString()
            stack.currentItem.location.text = url.substring(8, url.length)
        }

    }

    Connections {
        target: connector

        function onLog(message) {
            updateMessage(message)
        }

        function onUpdate(percent) {
            updatePercent(percent)
        }

        function onUpdateLocation(location) {
            stack.currentItem.location.text = location
        }

        function onDone(level) {
            if(level === 3) {
                proceedAfterServerInstallation()
            } else if(level === 5) {
                proceedAfterMySqlInstallation()
            } else if(level === 6) {
                proceedAfterPhpInstallation()
            } else if(level === 7) {
                proceedAfterFinalising()
            }
        }
    }

}
