import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Controls.Universal 2.3
import QtQuick.Layouts 1.3
import "components" as Comp

ApplicationWindow {
    visible: true
    width: 800
    height: 500

    title: qsTr("Welcome | Peter Setup")
    color: "darkgrey"

    Universal.theme: Universal.Dark

    property string message: qsTr("Log Info")

    signal declineLicensing()
    signal acceptLincense()

    signal useDefaultLocation()
    signal declineLocation()
    signal proceedAfterLocation()

    signal stopServerInstallation()
    signal proceedAfterServerInstallation()

    signal stopMySqlInstallation()
    signal proceedAfterMySqlInstallation()

    signal stopPhpInstallation()
    signal proceedAfterPhpInstallation()

    signal rejectAuthentication()
    signal proceedAfterAuth()

    signal rejectFinalising()
    signal proceedAfterFinalising()

    SwipeView {
        anchors.fill: parent
        currentIndex: 1

        RowLayout {
            //anchors.fill: parent
            spacing: 4

            Rectangle {
                Layout.preferredWidth: 200
                Layout.fillHeight: true

                Rectangle {
                    anchors.fill: parent

                    Image {
                        sourceSize: Qt.size(parent.width, parent.height)
                        source: "../images/img102.jpg"
                        fillMode: Image.PreserveAspectCrop
                    }

                }

            }

            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true

                ColumnLayout {
                    anchors.fill: parent
                    spacing: 0

                    Rectangle {
                        Layout.fillWidth: true
                        Layout.preferredHeight: 48

                        TabBar {
                            width: parent.width
                            height: parent.height

                            TabButton {
                                text: qsTr("Welcome")
                            }

                            TabButton {
                                text: qsTr("Location")
                            }

                            TabButton {
                                text: qsTr("Finish")
                            }

                        }

                    }

                    Rectangle {
                        Layout.fillWidth: true
                        Layout.fillHeight: true

                        Comp.Welcome {id: welcomeComp}
                        Comp.Location {id: locationComp}
                        Comp.Server {id: serverComp}
                        Comp.Authenticate {id: authComp}
                        Comp.MySql {id: mysqlComp}
                        Comp.Php {id: phpComp}
                        Comp.Finalising {id: finalComp}

                        StackView {
                            anchors.fill: parent
                            initialItem: welcomeComp
                        }
                    }

                }

            }

        }

        Comp.Appreciation {}

    }

}
