import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.4
import "../others" as Others

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

                ColumnLayout {
                    anchors.top: parent.top
                    anchors.bottom: parent.bottom
                    anchors.left: parent.left
                    anchors.right: parent.right
                    anchors.margins: 24
                    spacing: 16

                    Text {
                        topPadding: -12
                        text: qsTr("Authenticate Mysql")
                        font.family: "Segoe UI Semilight"
                        font.pixelSize: 14
                        color: "white"
                    }

                    Column {
                        spacing: 8
                        Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter

                        RowLayout {
                            width: 340
                            height: 28

                            Text {
                                height: parent.height
                                verticalAlignment: Text.AlignVCenter
                                text: "Enter Password"
                                font.family: "Segoe UI Semilight"
                                font.pixelSize: 14
                                color: "white"
                            }

                            Others.PassField {
                                Layout.alignment: Qt.AlignRight
                            }
                        }

                        RowLayout {
                            width: 340
                            height: 28

                            Text {
                                height: parent.height
                                verticalAlignment: Text.AlignVCenter
                                text: "Re-Enter Password"
                                font.family: "Segoe UI Semilight"
                                font.pixelSize: 14
                                color: "white"
                            }

                            Others.PassField {
                                Layout.alignment: Qt.AlignRight

                            }
                        }


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
