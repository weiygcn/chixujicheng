import os.path
import os

warSourcePathFile = 'D:\\java\\java_workspace\\doctor-manage\\target\\doctor-manage.war'
os.chdir('D:\\java\\java_workspace\\doctor-manage')
print('###################执行clean清楚原有打包信息')
os.system('mvn clean')
print('###################执行package打包war包')
os.system('mvn package')
print('###################开始清理tomcat webapp路径下的war包')
tomcatWar = 'D:\\java\\java_workspace\\apache-tomcat-8.5.23\\webapps\\doctor-manage.war'
print('###################检测tomcat webapp路径下是否存在war包')
if os.path.exists(tomcatWar):
    print('###################检测到旧war包，执行清理tomcat webapp路径下的war包')
    os.remove(tomcatWar)

else:
    print('###################检测无旧war包信息，不执行清理tomcat webapp路径下的war包')

if os.path.exists(warSourcePathFile):
    print('###################Maven打包成功')
    targePathFile = 'D:\\java\java_workspace\\apache-tomcat-8.5.23\\webapps\\doctor-manage.war'
    with open(targePathFile, 'wb') as f:
        f.write(open(warSourcePathFile, 'rb').read())

    if os.path.getsize(targePathFile) == os.path.getsize(warSourcePathFile):
        print('###################检测-拷贝成功')
        print('###################执行启动项目')
        os.system('D:\\java\\java_workspace\\apache-tomcat-8.5.23\\bin\startup.bat')
