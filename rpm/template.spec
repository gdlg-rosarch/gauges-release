Name:           ros-kinetic-gauges
Version:        1.0.5
Release:        0%{?dist}
Summary:        ROS gauges package

Group:          Development/Libraries
License:        See License.txt
URL:            http://wiki.ros.org/gauges
Source0:        %{name}-%{version}.tar.gz

Requires:       qt-devel
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-std-msgs
BuildRequires:  qt-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-std-msgs

%description
Launch virtual gauges for ROS topics.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Dec 01 2016 andyz <andyz@utexas.edu> - 1.0.5-0
- Autogenerated by Bloom

* Wed Nov 30 2016 andyz <andyz@utexas.edu> - 1.0.4-0
- Autogenerated by Bloom

* Wed Nov 30 2016 andyz <andyz@utexas.edu> - 1.0.3-0
- Autogenerated by Bloom

* Fri Nov 11 2016 andyz <andyz@utexas.edu> - 1.0.2-0
- Autogenerated by Bloom

* Wed Nov 09 2016 andyz <andyz@utexas.edu> - 1.0.1-0
- Autogenerated by Bloom

