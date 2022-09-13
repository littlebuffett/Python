from yattag import Doc
import product_info as cp

# product_keyword = input('키워드를 입력해주세요:')
# data = cp.get_products_search(product_keyword)

title = '1. 삼성전자 2021 노트북 플러스2 15.6'
sub_title = '퓨어 화이트, 셀러론, NVMe128GB, 8GB, WIN10 Pro, NT550XDA-K14AW'
body_text = [ '유튜브 시청, 가벼운 웹 서핑이 목적이라면 삼성전자의 플러스2를 추천한다. 부담없는 가격에 준수한 성능을 보여주는 노트북이다.',
    'pls 패널을 사용하여 어느 각도에서나 화면이 잘 보인다. 햇빛이 강한 카페에서도 사용할 수 있을 듯 하다.',
    'CPU로는 셀러론 6200을 사용했다. CPU의 성능이 궁금하면 다음의 링크를 참조하기 바란다. 참고로 노트북의 CPU와 일반 CPU는 다르니 이를 참고해야 한다.',
    '램을 8g로 유튜브 시청이나, 문서작업을 하는데 충분한 크기이다.',
    '가성비 노트북 추천 1위로 추천한다.']

img = 'https://masteryking.com/wp-content/uploads/2022/08/5375430731201828-5447a1be-7cd4-4fa7-a4a4-d960a4c2aac1-1'
img_alt = '노트북'
block_title = '삼성전자 2021 노트북 플러스2 15.6'
block_text = '삼성전자 플러스2는 15.6인치, pls패널, 샐러론 6200U의 준수한 성능을 가진 노트북이다. 가벼운 작업, 이를테면 유튜브 시청이나, 문서작업을 위해서라면 위의 사양만으로도 충분하다. 게다가 8G의 램을 갖고 있기 때문에 버벅거리지 않을 것이다. 가성비 제품을 찾는다면 이 제품을 찾아보는 것이 어떨까.'
product_url = ''


def make_src(src):
    return src + "-1024x1024.jpg"

def make_srcset(src):
    srcset = src + "-1024x1024.jpg 1024w, " + src + "-300x300.jpg 300w, " \
        + src + "-150x150.jpg 150w, " + src + "-768x768.jpg 768w, " \
        + src + "-1140x1140.jpg 1140w, " + src + "-920x920.jpg 920w, " \
        + src + "-575x575.jpg 575w, " + src + "-380x380.jpg 380w, " + src + ".jpg 1200w"
    return srcset

# 상품 정보를 받아 post작성
def write_wp_post(products):

    doc, tag, text = Doc().tagtext()

    for product in products:
        title = product['title']
        sub_title = product['sub_title']
        # body_text = 
        # img = 
        # img_alt = 
        # block_title = 
        # block_text =
        # product_url = 
    
        with tag('div', klass="entry-content" ):
            with tag('h2', klass="has-text-color has-larger-font-size" \
                , style="color:#e2127a;font-style:normal;font-weight:800"):
                text(title)
            with tag('h3', klass="has-color-1-color has-text-color has-large-font-size"):
                text(sub_title)
            for s in body_text:
                with tag('p'):
                    text(s)
            with tag('hr', klass="wp-block-separator has-alpha-channel-opacity is-style-wide"):
                pass
            with tag('div', klass="wp-block-media-text alignwide is-stacked-on-mobile"\
                    ,style="grid-template-columns:37% auto"):
                with tag('figure', klass="wp-block-media-text__media"):
                    with tag('img', loading="lazy", width="1024" ,height="1024", src=make_src(img),\
                        alt=img_alt, klass="wp-image-70 size-full", srcset=make_srcset(img),\
                        sizes="(max-width: 1024px) 100vw, 1024px"):
                        pass
                with tag('div', klass="wp-block-media-text__content"):
                    with tag('h3', klass="has-text-color has-larger-font-size", style="color:#e2127a"):
                        text(block_title)
                    with tag('p'):
                        text(block_text)
                    with tag('div', klass="wp-container-3 wp-block-buttons"):
                        with tag('div', klass="wp-block-button"):
                            with tag('a', klass="wp-block-button__link", href=product_url):
                                text('최저가 구매하러 가기')
                with tag('p', id = 'main'):
                    text('some text')
                with tag('a', href='/my-url'):
                    text('some link')

        result = doc.getvalue()
        file = open("product.txt", "w") 
        file.write(result)
        file.close()