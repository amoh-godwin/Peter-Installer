import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

Rectangle {
    color: "black"

    ColumnLayout {
        width: parent.width
        height: parent.height

        Rectangle {
            Layout.alignment: Qt.AlignTop
            Layout.fillWidth: true
            Layout.preferredHeight: 124
            clip: true

            Image {
                sourceSize: Qt.size(parent.width, parent.height)
                source: "../../images/img102.jpg"
                fillMode: Image.PreserveAspectFit
                clip: true
            }

        }

        Text {
            padding: 24
            Layout.fillHeight: true
            font.family: "Segoe UI Semilight"
            font.pixelSize: 14
            text: qsTr("Setup Complete")
            color: "white"
        }

        Rectangle {
            Layout.fillWidth: true
            Layout.preferredHeight: 56
            color: "dodgerblue"

            Row {
                anchors.right: parent.right
                anchors.rightMargin: 12
                anchors.verticalCenter: parent.verticalCenter
                spacing: 4

                Button {
                    text: qsTr("Close Setup")

                    onClicked: {
                        closeSetup();
                    }

                }

                Button {
                    text: qsTr("Launch Application")

                    onClicked: {
                        launchApplication();
                    }

                }

            }

        }

    }

}
