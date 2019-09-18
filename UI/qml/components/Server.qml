import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.4

Component {

    Rectangle {
        anchors.fill: parent

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
                        text: qsTr("Installing Server")
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
                            width: (parent.width / 100) * 8
                            height: parent.height
                            color: "dodgerblue"
                            clip: true
                        }

                    }

                    Text {
                        topPadding: -16
                        text: qsTr("Please wait")
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
                    }

                    Button {
                        text: qsTr("Next")
                    }

                }

            }

        }

    }

}

