import QtQuick 2.10
import QtQuick.Controls 2.3
import QtQuick.Layouts 1.3

ApplicationWindow {
    visible: true
    width: 800
    height: 500
    color: "darkgrey"

    RowLayout {
        anchors.fill: parent

        Rectangle {
            Layout.preferredWidth: 200
            Layout.fillHeight: true

            Rectangle {
                anchors.fill: parent

                Image {
                    sourceSize: Qt.size(parent.width, parent.height)
                    source: ""
                }

            }

        }

        Rectangle {
            Layout.fillWidth: true
            Layout.fillHeight: true
        }

    }

}
