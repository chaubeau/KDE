#include <QtGui/QApplication>
#include "T3.h"


int main(int argc, char** argv)
{
    QApplication app(argc, argv);
    T3 foo;
    foo.show();
    return app.exec();
}
