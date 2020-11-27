# MySQLdbのインポート
import MySQLdb

def create_pdb():
    # データベースへの接続とカーソルの生成
    connection = MySQLdb.connect(
    host='mysql',
    user='root',
    passwd='root',
    db='db',
    # テーブル内部で日本語を扱うために追加
    charset='utf8'
    )
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS Cpu")
    cursor.execute("DROP TABLE IF EXISTS Motherboard")
    cursor.execute("DROP TABLE IF EXISTS SSD")
    cursor.execute("DROP TABLE IF EXISTS Memory")
    cursor.execute("DROP TABLE IF EXISTS HDD")
    cursor.execute("DROP TABLE IF EXISTS Cases")
    cursor.execute("DROP TABLE IF EXISTS Power")
    cursor.execute("DROP TABLE IF EXISTS cpuCooler")
    cursor.execute("DROP TABLE IF EXISTS caseCooler")
    cursor.execute("DROP TABLE IF EXISTS Price")
    cursor.execute("DROP TABLE IF EXISTS Website")
    cursor.execute("DROP TABLE IF EXISTS Maker")
    cursor.execute("DROP TABLE IF EXISTS Category")

    # Category table
    cursor.execute("""CREATE TABLE Category(
                        category_id       INT not null,
                        category_name     VARCHAR(20),
                        primary key(category_id)
                    )""")

    cursor.execute("""INSERT INTO Category (category_id, category_name)
        VALUES (1, 'cpu'),
            (2, 'motherboard'),
            (3, 'memory'),
            (4, 'ssd'),
            (5, 'hdd'),
            (6, 'case'),
            (7, 'gpu'),
            (8, 'power'),
            (9, 'cpucooler'),
            (10,'fan')
        """)

    # Maker table
    cursor.execute("""CREATE TABLE Maker(
                        maker_id       INT not null,
                        maker_name     VARCHAR(50),
                        primary key(maker_id)
                    )""")

    cursor.execute("""INSERT INTO Maker (maker_id, maker_name)
        VALUES (101, 'intel'),
            (102, 'amd'),
            (103, 'mother'),
            (104, 'memory'),
            (105, 'ssd'),
            (106, 'hdd'),
            (107, 'case'),
            (109, 'power'),
            (110, 'cpucooler'),
            (111, 'fan')
        """)

    # Website table
    cursor.execute("""CREATE TABLE Website(
                        web_id       INT not null,
                        web_name     VARCHAR(50),
                        primary key(web_id)
                    )""")
    cursor.execute("""INSERT INTO Website (web_id, web_name)
        VALUES (201, 'dospara'),
            (202, 'amazon')
        """)

    #外部参照　参考ページ https://qiita.com/SLEAZOIDS/items/d6fb9c2d131c3fdd1387



    # Price table
    cursor.execute("""CREATE TABLE Price(
                        product_id     INT,
                        web_id         INT,
                        price          int,
                        url            varchar(300),
                        category_id      INT,
                        primary key (product_id,web_id),
                        constraint fk_web_id
                        foreign key (web_id)
                        references Website (web_id)
                        ON UPDATE CASCADE,
                        constraint fk_price_category_id
                        foreign key (category_id)
                        references Category (category_id)
                        on update cascade
                    )""")
    #外部キー削除　ALTER TABLE テーブル名 DROP FOREIGN KEY 制約の名前(fk_web_id);

    # Cpu table

    cursor.execute("""CREATE TABLE Cpu(
                        product_id       INT,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        info             VARCHAR(500),
                        maker_id         INT,
                        socket           varchar(20),
                        clock            varchar(20),
                        thread             int,
                        core             int,
                        TDP              int,
                        constraint pk_cpu_product
                        primary key (product_id),
                        constraint fk_mother_maker
                        foreign key (maker_id)
                        references Maker (maker_id)
                        on delete set null
                        on update cascade
                    )""")


    # Motherboard table

    cursor.execute("""CREATE TABLE Motherboard(
                        product_id       INT,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        info             VARCHAR(500),
                        maker_id         INT,
                        socket           varchar(20),
                        clock            varchar(20),
                        chipset          varchar(20),
                        Supported_memory varchar(20),
                        Maximum_memory   int,
                        foamfactor       varchar(50),
                        constraint pk_mother_product
                        primary key (product_id),
                        constraint fk_mother_makerm
                        foreign key (maker_id)
                        references Maker (maker_id)
                        on delete set null
                        on update cascade
                    )""")


    # SSD table

    cursor.execute("""CREATE TABLE SSD(
                        product_id       INT,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        info             VARCHAR(500),
                        maker_id         INT,
                        connection       varchar(50),
                        capacity         int,
                        size             varchar(50),
                        max_write        int,
                        max_read         int,
                        constraint pk_ssd_product
                        primary key (product_id),
                        constraint fk_ssd_makerm
                        foreign key (maker_id)
                        references Maker (maker_id)
                        on delete set null
                        on update cascade
                    )""")


    # Memory table

    cursor.execute("""CREATE TABLE Memory(
                        product_id       INT,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        info             VARCHAR(500),
                        maker_id         INT,
                        capacity         int,
                        standard         varchar(20),
                        speed            varchar(20),
                        constraint pk_memory_product
                        primary key (product_id),
                        constraint fk_memory_makerm
                        foreign key (maker_id)
                        references Maker (maker_id)
                        on delete set null
                        on update cascade
                    )""")

    # HDD table

    cursor.execute("""CREATE TABLE HDD(
                        product_id       INT,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        info             VARCHAR(500),
                        maker_id         INT,
                        capacity         int,
                        connect          varchar(50),
                        rotation_speed   varchar(50),
                        cache            varchar(50),
                        size             varchar(50),
                        constraint pk_hdd_product
                        primary key (product_id),
                        constraint fk_hdd_makerm
                        foreign key (maker_id)
                        references Maker (maker_id)
                        on delete set null
                        on update cascade
                    )""")

    # Case table

    cursor.execute("""CREATE TABLE Cases(
                        product_id       INT,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        info             VARCHAR(500),
                        maker_id         INT,
                        corresponding_case_size varchar(50),
                        expansion_slot   varchar(50),
                        bay              varchar(50),
                        constraint pk_case_product
                        primary key (product_id),
                        constraint fk_case_makerm
                        foreign key (maker_id)
                        references Maker (maker_id)
                        on delete set null
                        on update cascade
                    )""")

    # Power table

    cursor.execute("""CREATE TABLE Power(
                        product_id       INT,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        info             VARCHAR(700),
                        maker_id         INT,
                        integrated_output varchar(50),
                        authentication   varchar(50),
                        corresponding_standard varchar(50),
                        constraint pk_power_product
                        primary key (product_id),
                        constraint fk_power_makerm
                        foreign key (maker_id)
                        references Maker (maker_id)
                        on delete set null
                        on update cascade
                    )""")

    #cpuCooler  table

    cursor.execute("""CREATE TABLE cpuCooler(
                        product_id       INT,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        info             VARCHAR(700),
                        maker_id         INT,
                        compatible_socket varchar(150),
                        fan_numberofrotations   varchar(110),
                        noise            varchar(100),
                        air_flow         varchar(50),
                        constraint pk_air_product
                        primary key (product_id),
                        constraint fk_air_makerm
                        foreign key (maker_id)
                        references Maker (maker_id)
                        on delete set null
                        on update cascade
                    )""")

    #caseCooler  table

    cursor.execute("""CREATE TABLE caseCooler(
                        product_id       INT,
                        product_name     VARCHAR(200),
                        image            VARCHAR(300),
                        info             VARCHAR(700),
                        maker_id         INT,
                        size             varchar(50),
                        fan_numberofrotations   varchar(110),
                        noise            varchar(100),
                        air_flow         varchar(50),
                        constraint pk_cco_product
                        primary key (product_id),
                        constraint fk_cco_makerm
                        foreign key (maker_id)
                        references Maker (maker_id)
                        on delete set null
                        on update cascade
                    )""")

    # 保存を実行
    connection.commit()

    # 接続を閉じる
    connection.close()


