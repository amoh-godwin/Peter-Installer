import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3
import "../others" as Others

Component {

    Rectangle {
        id: cont

        property QtObject field1
        property QtObject field2

        Component.onCompleted: stage = 4

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

                                Component.onCompleted: cont.field1 = this

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

                                Component.onCompleted: cont.field2 = this

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

                        onClicked: {
                            rejectAuthentication();
                        }

                    }

                    Button {
                        text: qsTr("Next")

                        onClicked: {
                            proceedAfterAuth();
                        }

                    }

                }

            }

        }

    }

}
