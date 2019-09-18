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
                                text: "/path/to/Server"
                                color: "white"

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
                    }

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

