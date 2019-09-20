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

            }

            Rectangle {
                Layout.fillWidth: true
                Layout.preferredHeight: 56
                color: "black"

                Row {
                    anchors.centerIn: parent
                    spacing: 4

                    Button {
                        text: qsTr("Decline")
                    }

                    Button {
                        text: qsTr("Accept")
                    }

                }

            }

        }

    }

}
