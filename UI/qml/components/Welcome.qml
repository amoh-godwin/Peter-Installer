import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

Component {

    Rectangle {

        Component.onCompleted: {
            stage = 1
        }

        ColumnLayout {
            anchors.fill: parent
            spacing: 0

            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "black"

                ScrollView {
                    anchors.fill: parent
                    ScrollBar.horizontal.active: false
                    anchors.margins: 28
                    clip: true

                    TextArea {
                        width: 400
                        bottomPadding: 12
                        color: "white"
                        font.family: "Segoe UI Semilight"
                        font.pixelSize: 14
                        wrapMode: Text.WordWrap
                        text: license_text
                        readOnly: true
                        activeFocusOnPress: false
                        activeFocusOnTab: false
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
                        text: qsTr("Decline")

                        onClicked: {
                            declineLicensing();
                        }

                    }

                    Button {
                        text: qsTr("Accept")

                        onClicked: {
                            acceptLincense();
                        }

                    }

                }

            }

        }

    }

}
