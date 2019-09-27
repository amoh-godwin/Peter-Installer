import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

Component {

    Rectangle {
        id: cont

        property int progress_percent: 4
        property bool done: true


        Component.onCompleted: {
            stage = 6;
            done = false;
            startPhpInstallation()
        }

        ColumnLayout {
            anchors.fill: parent
            spacing: 0

            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "black"

                Column {
                    anchors.top: parent.top
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.margins: 24
                    spacing: 16

                    Text {
                        text: qsTr("Installing Php")
                        font.family: "Segoe UI Semilight"
                        font.pixelSize: 14
                        color: "white"
                    }

                    Rectangle {
                        width: parent.width
                        height: 8
                        border.color: Qt.rgba(255, 255, 255, 0.2)
                        color: "transparent"

                        Rectangle {
                            width: (parent.width / 100) * cont.progress_percent
                            height: parent.height
                            color: "dodgerblue"
                            clip: true
                        }

                    }

                    Text {
                        topPadding: -16
                        text: message
                        font.family: "Segoe UI Semilight"
                        font.pixelSize: 12
                        color: "white"
                    }

                }

            }

            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: 56
                color: "black"

                Row {
                    anchors.centerIn: parent
                    spacing: 4

                    Button {
                        text: qsTr("Back")

                        onClicked: {
                            stopPhpInstallation();
                        }

                    }

                    Button {
                        text: qsTr("Next")
                        enabled: done

                        onClicked: {
                            proceedAfterPhpInstallation();
                        }

                    }

                }

            }

        }

    }

}

