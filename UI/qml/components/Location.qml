import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

Component {

    Rectangle {
        property QtObject location

        Component.onCompleted: {
            stage = 2
            useDefaultLocation()
        }

        ColumnLayout {
            anchors.fill: parent
            spacing: 0

            Rectangle {
                Layout.fillWidth: true
                Layout.fillHeight: true
                color: "black"

                Rectangle {
                    anchors.centerIn: parent
                    width: 500
                    height: 52
                    color: "transparent"

                    Column {
                        anchors.fill: parent

                        Row {
                            spacing: 4

                            TextField {
                                text: ""
                                color: "white"

                                Component.onCompleted: {
                                    location = this
                                }

                                background: Rectangle {
                                    implicitWidth: 380
                                    implicitHeight: 20
                                    color: "transparent"
                                    border.color: "white"
                                    radius: 2
                                }

                            }

                            Button {
                                text: "Browse"

                                onClicked: {
                                    folder_picker.open()
                                }

                            }

                        }

                        Text {
                            text: qsTr("Nice path")
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
                        text: qsTr("Use Default")

                        onClicked: {
                            useDefaultLocation();
                        }

                    }

                    Button {
                        text: qsTr("Back")

                        onClicked: {
                            declineLocation();
                        }

                    }

                    Button {
                        text: qsTr("Next")

                        onClicked: {
                            proceedAfterLocation();
                        }

                    }

                }

            }

        }

    }

}

