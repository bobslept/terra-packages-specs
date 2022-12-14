# Generated by rust2rpm 23
%bcond_without check

%global crate starship

Name:           rust-starship
Version:        1.12.0
Release:        %autorelease
Summary:        Minimal, blazing-fast, and infinitely customizable prompt for any shell! ☄🌌️

License:        ISC
URL:            https://crates.io/crates/starship
Source:         %{crates_source}
# Automatically generated patch to strip foreign dependencies
Patch:          starship-fix-metadata-auto.diff

BuildRequires:  rust-packaging >= 21
BuildRequires:  anda-srpm-macros
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  git-core

%global _description %{expand:
Minimal, blazing-fast, and infinitely customizable prompt for any shell! ☄🌌️.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md
%{_bindir}/starship

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+battery-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+battery-devel %{_description}

This package contains library source intended for building other packages which
use the "battery" feature of the "%{crate}" crate.

%files       -n %{name}+battery-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+config-schema-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+config-schema-devel %{_description}

This package contains library source intended for building other packages which
use the "config-schema" feature of the "%{crate}" crate.

%files       -n %{name}+config-schema-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+git-features-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+git-features-devel %{_description}

This package contains library source intended for building other packages which
use the "git-features" feature of the "%{crate}" crate.

%files       -n %{name}+git-features-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+git-repository-faster-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+git-repository-faster-devel %{_description}

This package contains library source intended for building other packages which
use the "git-repository-faster" feature of the "%{crate}" crate.

%files       -n %{name}+git-repository-faster-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+git-repository-max-perf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+git-repository-max-perf-devel %{_description}

This package contains library source intended for building other packages which
use the "git-repository-max-perf" feature of the "%{crate}" crate.

%files       -n %{name}+git-repository-max-perf-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+notify-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+notify-devel %{_description}

This package contains library source intended for building other packages which
use the "notify" feature of the "%{crate}" crate.

%files       -n %{name}+notify-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+notify-rust-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+notify-rust-devel %{_description}

This package contains library source intended for building other packages which
use the "notify-rust" feature of the "%{crate}" crate.

%files       -n %{name}+notify-rust-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+schemars-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+schemars-devel %{_description}

This package contains library source intended for building other packages which
use the "schemars" feature of the "%{crate}" crate.

%files       -n %{name}+schemars-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+starship-battery-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+starship-battery-devel %{_description}

This package contains library source intended for building other packages which
use the "starship-battery" feature of the "%{crate}" crate.

%files       -n %{name}+starship-battery-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
