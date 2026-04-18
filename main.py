<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>喵圈 CatBBS - Melody's Project</title>
  <style>
    :root{
      --bg:#fff8fb; --bg-2:#fff3f8; --card:#ffffff; --line:#f2d6e4; --text:#3b3340; --sub:#7e6f79;
      --pink:#ff7eb6; --pink-2:#ffb3d2; --pink-3:#ffe1ee; --accent:#8f7cff; --green:#6ccf9b;
      --orange:#ffb35c; --red:#ff6f7f; --shadow:0 12px 30px rgba(255,126,182,.12);
      --radius:18px; --max:1200px;
    }
    *{box-sizing:border-box}
    html,body{margin:0;padding:0;background:linear-gradient(180deg,var(--bg),#fff);color:var(--text);font-family:-apple-system,sans-serif;min-height:100vh;}
    button,input,textarea,select{font:inherit;outline:none;}
    a{text-decoration:none;color:inherit}

    .topbar{position:sticky;top:0;z-index:20;backdrop-filter:blur(12px);background:rgba(255,248,251,.82);border-bottom:1px solid rgba(242,214,228,.9);}
    .topbar-inner{max-width:var(--max);margin:0 auto;padding:14px 20px;display:flex;align-items:center;justify-content:space-between;gap:16px;}
    .brand{display:flex;align-items:center;gap:12px;cursor:pointer;}
    .brand-logo{width:42px;height:42px;border-radius:14px;background:linear-gradient(135deg,var(--pink),var(--accent));color:#fff;display:grid;place-items:center;font-size:22px;}
    .brand-title{font-size:18px;font-weight:800;}
    .brand-sub{font-size:12px;color:var(--sub);margin-top:3px;}

    .btn{border:none;border-radius:14px;padding:10px 14px;background:#fff;color:var(--text);cursor:pointer;border:1px solid var(--line);transition:.18s;display:inline-flex;align-items:center;gap:8px;font-weight:600;}
    .btn:hover{transform:translateY(-1px);box-shadow:var(--shadow)}
    .btn-primary{background:linear-gradient(135deg,var(--pink),#ff91c1);color:#fff;border:none;}
    .btn-sm{padding:6px 12px;border-radius:10px;font-size:13px}
    .btn-ai{background:linear-gradient(135deg,var(--accent),#a697ff);color:#fff;border:none;}

    .layout{max-width:var(--max);margin:0 auto;padding:20px;display:grid;grid-template-columns:260px 1fr 280px;gap:20px;}
    .panel{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:16px;margin-bottom:16px;}

    .chip{display:inline-flex;align-items:center;gap:6px;padding:4px 10px;border-radius:999px;background:var(--pink-3);color:#a04b72;font-size:12px;font-weight:700;}
    .chip-gray{background:#f7f5f7;color:#7b6c76}
    .chip-green{background:#ebfff5;color:#258156}
    .chip-orange{background:#fff6e9;color:#a56600}

    .nav-item{padding:12px 14px;border-radius:14px;cursor:pointer;display:flex;align-items:center;gap:10px;transition:.2s;}
    .nav-item:hover{background:var(--bg-2)}
    .nav-item.active{background:linear-gradient(180deg,#fff,#fff4f8);border:1px solid #ffd4e6;color:#a53f70;font-weight:700;}

    .post-card{border:1px solid var(--line);border-radius:20px;padding:16px;margin-bottom:16px;background:#fff;transition:0.2s;}
    .post-card:hover{box-shadow:var(--shadow)}
    .avatar{width:48px;height:48px;border-radius:16px;background:#ffe6ef;display:flex;align-items:center;justify-content:center;font-size:24px;border:1px solid #ffd7e5;position:relative;}
    .avatar.large{width:80px;height:80px;font-size:40px;border-radius:24px;}
    .accessory{position:absolute;top:-10px;right:-5px;font-size:0.8em;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.2));}

    .field{margin-bottom:16px;}
    .field label{display:block;font-size:13px;font-weight:700;margin-bottom:6px;color:#5f4f59}
    .input-box{width:100%;border:1px solid var(--line);background:#fff;border-radius:14px;padding:12px 14px;transition:.2s;}
    .input-box:focus{border-color:var(--pink);box-shadow:0 0 0 4px rgba(255,126,182,.1)}

    .toast-wrap{position:fixed;top:80px;left:50%;transform:translateX(-50%);display:flex;flex-direction:column;gap:10px;z-index:999;pointer-events:none;}
    .toast{background:#fff;border:1px solid var(--pink);border-radius:14px;padding:12px 24px;box-shadow:0 10px 30px rgba(255,126,182,.3);font-weight:bold;color:var(--pink);animation:slideDown 0.3s ease forwards;}
    @keyframes slideDown { from{transform:translateY(-20px);opacity:0} to{transform:translateY(0);opacity:1} }

    .melody-footer { text-align:center; padding: 30px 20px; color: var(--sub); font-size: 14px; border-top: 1px dashed var(--line); margin-top: 20px; }
    .melody-footer a { color: var(--pink); font-weight: bold; text-decoration: underline; margin-left: 5px; }

    @media (max-width: 900px){
      .layout{grid-template-columns:1fr;}
      .sidebar, .rightbar {display:none;}
    }
  </style>
</head>
<body>
  <div id="app"></div>
  <div id="toast-root" class="toast-wrap"></div>

  <script>
    const STORAGE_KEY = "catbbs_v5_final";
    const defaultData = {
      currentUser: null,
      view: 'auth', params: {},
      users: [
        { id: 'u1', name: '糯米团', avatar: '🐱', accessory: '', breed: '英短', age: '2岁', city: '上海', bio: '白天晒太阳，晚上看聊天。', abebei: '小黄毯', tags: ['黏人'], follows: [], followers: [], places: [{name:'滨江步道', status:'去过', review:'风很轻'}] },
        { id: 'u2', name: '栗子', avatar: '😽', accessory: '🎀', breed: '田园猫', age: '1岁半', city: '杭州', bio: '晚安楼常驻。', abebei: '小鱼', tags: ['活泼'], follows: ['u1'], followers: [], places: [] },
        { id: 'u3', name: '奶盐', avatar: '😿', accessory: '👑', breed: '银渐层', age: '3岁', city: '成都', bio: '旅行派小猫。', abebei: '旧帆布包', tags: ['慢热', '爱旅行'], follows: ['u1'], followers: [], places: [{name:'麓湖', status:'去过', review:'草地有太阳味'}] }
      ],
      boards: [{ id: 'daily', name: '日常生活', icon: '☁️' }, { id: 'companion', name: '晚安楼', icon: '🌙' }],
      posts: [
        { id: 'p1', authorId: 'u3', boardId: 'daily', title: '[测评] 喵生巅峰！这款主食罐头我愿称之为地表最强', content: '铲屎的终于开窍了，买了这款高肉含量的罐头。肉质紧实，闻起来比主人的外卖香多了！喵呜~ 强烈推荐给各位追求生活品质的喵友。', tags: ['好物分享', '罐头测评'], likes: ['u1', 'u2'], replies: [{authorId:'u1', content:'看起来好香，我也要去暗示一下我主人！', time: Date.now()-3000000}], time: Date.now() - 3600000 },
        { id: 'p2', authorId: 'u1', boardId: 'daily', title: '避雷！这款猫爬架太晃了，差点摔坏我的小屁股', content: '大家千万别买那个蓝色的三层爬架。我刚才一个加速起跳，整个架子都在颤抖。这届人类做工太粗糙了，建议还是老老实实买实木的。', tags: ['避雷', '猫用品'], likes: ['u3'], replies: [], time: Date.now() - 7200000 },
        { id: 'p3', authorId: 'u2', boardId: 'companion', title: '晚安楼：今天的梦里会有吃不完的冻干吗？', content: '月亮已经挂在窗户角了。我数了数，外面亮了三盏灯。希望今晚梦里，冻干能从天上掉下来，正好掉进我的碗里。', tags: ['晚安', '轻陪伴'], likes: ['u1', 'u3'], replies: [{authorId:'u3', content:'肯定会的，好猫猫都会有好梦！', time: Date.now()-8000000}], time: Date.now() - 10800000 },
        { id: 'p4', authorId: 'u1', boardId: 'daily', title: '今日阿贝贝观察：我的小黄毯还是那么软喵~', content: '洗香香之后的小黄毯有一股阳光的味道。这是我最珍贵的阿贝贝，谁都不能抢走，哪怕是家里的那只扫地机器人也不行！', tags: ['阿贝贝', '日常'], likes: ['u2'], replies: [], time: Date.now() - 14400000 },
        { id: 'p5', authorId: 'u3', boardId: 'daily', title: '论一个自动饮水机如何激发本猫的捕猎本能', content: '那个流水的声音，让我觉得我正在野外的溪边。虽然它偶尔会发出奇怪的嗡嗡声，但喝水确实变有趣了。推荐给不爱喝水的小伙伴。', tags: ['饮水机', '好物分享'], likes: ['u1'], replies: [], time: Date.now() - 18000000 },
        { id: 'p6', authorId: 'u2', boardId: 'daily', title: '又是占领键盘的一天，主人怎么还不下班？', content: '我只是想提醒她该给我开罐头了。为什么她总是在那个发光的盒子上敲来敲去？我也来帮她敲几个字符：喵呜呜呜呜呜呜呜。', tags: ['摸鱼', '陪伴'], likes: ['u1', 'u3'], replies: [], time: Date.now() - 21600000 },
        { id: 'p7', authorId: 'u1', boardId: 'daily', title: '纸箱 vs 猫窝，我还是坚定选择快递盒！', content: '人类花了大价钱买的软绵绵猫窝，真的不如一个快递纸箱有灵魂。这里的磨爪感、这里的包裹感... 谁懂啊！', tags: ['真实', '拆家'], likes: ['u3'], replies: [], time: Date.now() - 25200000 },
        { id: 'p8', authorId: 'u3', boardId: 'daily', title: '[在途] 坐在主人电动车后座，风把我的胡须吹乱了', content: '我们要去外婆家。虽然躲在猫包里，但我能感觉到速度。外面的气味一直在变，这种感觉真刺激！', tags: ['旅行见闻', '在途'], likes: ['u1', 'u2'], replies: [], time: Date.now() - 28800000 },
        { id: 'p9', authorId: 'u2', boardId: 'companion', title: '只要有你陪着，窗外的雨声也像在演奏', content: '今天下雨了。主人坐在沙发上看书，我趴在她的腿上。听着雨声，闻着她的毛衣味，我觉得这个社区存在的意义就是分享这种瞬间。', tags: ['治愈', '陪伴'], likes: ['u1', 'u3'], replies: [], time: Date.now() - 32400000 },
        { id: 'p10', authorId: 'u1', boardId: 'companion', title: '谁能拒绝一只在午后阳光下疯狂踩奶的小猫呢？', content: '阳光、地毯、节奏感。这是我今天最解压的时刻。希望大家在忙碌的一天后，也能找到自己的节奏。', tags: ['踩奶', '陪伴楼'], likes: ['u2', 'u3'], replies: [], time: Date.now() - 36000000 },
        { id: 'p11', authorId: 'u3', boardId: 'daily', title: '去过：小区楼下的公园草坪，味道很清新', content: '今天第一次牵引绳散步。草地扎扎的，但是有很多飞来飞去的小虫子，我的眼睛都忙不过来了！推荐指数：四颗星。', tags: ['地点档案', '旅行'], likes: ['u1'], replies: [], time: Date.now() - 39600000 },
        { id: 'p12', authorId: 'u2', boardId: 'daily', title: '[好物] 这个逗猫棒竟然能飞出残影，我认输了', content: '强烈推荐那个带羽毛的长杆逗猫棒。铲屎官一挥，我差点飞到天花板上去。运动量达标，今晚能多吃一口冻干吗？', tags: ['好物分享', '解压'], likes: ['u1', 'u3'], replies: [], time: Date.now() - 43200000 },
        { id: 'p13', authorId: 'u1', boardId: 'daily', title: '[AI喵化] 关于如何优雅地在半夜三点跳迪斯科...', content: '喵呜！其实半夜跑酷是为了消耗白天多摄入的热量。建议各位喵友选择主人的肚皮作为起跳点，弹性十足，体验极佳。', tags: ['AI改写', '冷知识'], likes: ['u2'], replies: [], time: Date.now() - 46800000 },
        { id: 'p14', authorId: 'u3', boardId: 'daily', title: '[AI喵化] 人类总是觉得我听不懂话，其实我只是不想理', content: '只要不喊“罐头”和“开饭”，所有的呼唤对本猫来说都是白噪音。这就是猫咪的高冷艺术。', tags: ['深度思考', '喵设'], likes: ['u1'], replies: [], time: Date.now() - 50400000 },
        { id: 'p15', authorId: 'u2', boardId: 'daily', title: '想去：那个传说中有很多鱼的城市码头', content: '听主人说海边有很多新鲜的鱼。我已经把它标在我的想去清单里了，等哪天猫包一拉，我们就出发！', tags: ['想去清单', '旅行'], likes: ['u1', 'u3'], replies: [], time: Date.now() - 54000000 }
      ],
      notifications: []
    };

    let state = localStorage.getItem(STORAGE_KEY) ? JSON.parse(localStorage.getItem(STORAGE_KEY)) : JSON.parse(JSON.stringify(defaultData));
    const saveState = () => localStorage.setItem(STORAGE_KEY, JSON.stringify(state));

    const getUser = (id) => state.users.find(u => u.id === id) || state.users[0];
    const getPost = (id) => state.posts.find(p => p.id === id);
    const getBoard = (id) => state.boards.find(b => b.id === id);
    const formatTime = (ts) => {
      const diff = Date.now() - ts;
      if (diff < 60000) return '刚刚';
      if (diff < 3600000) return Math.floor(diff/60000) + '分钟前';
      if (diff < 86400000) return Math.floor(diff/3600000) + '小时前';
      return new Date(ts).toLocaleDateString();
    };
    const showToast = (msg, duration=2500) => {
      const div = document.createElement('div');
      div.className = 'toast'; div.innerText = msg;
      document.getElementById('toast-root').appendChild(div);
      setTimeout(() => { div.style.opacity = '0'; setTimeout(()=>div.remove(),300); }, duration);
    };

    const APP = document.getElementById('app');
    const render = () => {
      if (!state.currentUser && state.view !== 'auth') state.view = 'auth';
      APP.innerHTML = state.view === 'auth' ? renderAuthPage() : renderShell();
    };

    const renderAuthPage = () => `
      <div style="min-height:100vh;display:grid;place-items:center;padding:20px;">
        <div style="text-align:center;background:#fff;padding:40px;border-radius:24px;box-shadow:var(--shadow);max-width:500px;width:100%">
          <h1 style="color:var(--pink)">喵圈 CatBBS</h1>
          <p style="color:var(--sub);margin-bottom:30px">选择一只小猫，体验AIGC驱动的陪伴型社区</p>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:15px;margin-bottom:30px">
            ${state.users.slice(0,2).map(u => `
              <div style="border:1px solid var(--line);padding:20px;border-radius:16px;cursor:pointer" data-action="login" data-id="${u.id}">
                <div class="avatar" style="margin:0 auto 10px">${u.avatar}${u.accessory?`<div class="accessory">${u.accessory}</div>`:''}</div>
                <b>${u.name}</b>
              </div>
            `).join('')}
          </div>
          <button class="btn btn-primary" style="width:100%;justify-content:center" onclick="showToast('请点击上方的样板猫猫进入体验~')">注册新猫猫</button>
        </div>
      </div>
    `;

    const renderShell = () => `
      <div class="topbar">
        <div class="topbar-inner">
          <div class="brand" data-nav="home">🐾 <div class="brand-title">喵圈 CatBBS</div></div>
          <div style="display:flex;gap:10px;">
            <button class="btn btn-primary" data-nav="create">✍️ 发帖</button>
            <button class="btn" data-nav="profile" data-id="${state.currentUser}">😸 我的主页</button>
            <button class="btn" data-action="logout">退出</button>
          </div>
        </div>
      </div>
      <div class="layout">
        <aside class="sidebar">
          <div class="panel" style="position:sticky;top:90px">
            <h3>导航</h3>
            <div class="nav-item ${state.view==='home'?'active':''}" data-nav="home">🏠 推荐首页</div>
            ${state.boards.map(b => `<div class="nav-item ${state.view==='board' && state.params.id===b.id?'active':''}" data-nav="board" data-id="${b.id}">${b.icon} ${b.name}</div>`).join('')}
          </div>
        </aside>
        <main>${renderMain()}</main>
        <aside class="rightbar">
          <div class="panel" style="position:sticky;top:90px;cursor:pointer" data-action="view-risk">
            <h3>社区治理记录</h3>
            <div style="font-size:12px;color:var(--sub);line-height:1.6">
              🛡️ <b>AIGC风控系统运行中</b><br>
              今日拦截违规发帖: 0 条<br>
              自动折叠水贴: 2 条<br>
              <span style="color:var(--pink);text-decoration:underline;margin-top:5px;display:block">点击查看系统日志</span>
            </div>
          </div>
        </aside>
      </div>
      <div class="melody-footer">
        ✨ 感谢体验喵圈 MVP 版本 ✨<br>
        和开发者 Melody 说些什么呢：<a href="mailto:tangxiaoxuan24gz@yeah.net">tangxiaoxuan24gz@yeah.net</a>
      </div>
    `;

    const renderMain = () => {
      if (state.view === 'home') return renderFeed(state.posts, '推荐首页', '看看别的猫猫都在做什么。');
      if (state.view === 'board') {
         const board = getBoard(state.params.id);
         const boardPosts = state.posts.filter(p => p.boardId === board.id);
         return renderFeed(boardPosts, `${board.icon} ${board.name}`, `欢迎来到${board.name}板块喵~`);
      }
      if (state.view === 'detail') return renderDetail();
      if (state.view === 'profile') return renderProfile();
      if (state.view === 'edit-profile') return renderEditProfile();
      if (state.view === 'create') return renderCreate();
    };

    const renderFeed = (posts, title, sub) => `
      <div class="hero" style="margin-bottom:20px">
        <h1>${title}</h1><p>${sub}</p>
      </div>
      ${posts.length === 0 ? '<div class="panel" style="text-align:center;color:var(--sub);padding:40px">这个板块还很安静，快来发第一帖吧！</div>' : ''}
      ${posts.sort((a,b)=>b.time-a.time).map(p => {
        const author = getUser(p.authorId);
        return `
          <div class="post-card">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;cursor:pointer" data-nav="profile" data-id="${author.id}">
              <div class="avatar">${author.avatar}${author.accessory?`<div class="accessory">${author.accessory}</div>`:''}</div>
              <div><b>${author.name}</b> <span style="font-size:12px;color:var(--sub)">· ${formatTime(p.time)}</span></div>
            </div>
            <h2 class="post-title" data-nav="detail" data-id="${p.id}">${p.title}</h2>
            <div class="post-content">${p.content}</div>
            <div style="display:flex;gap:15px;margin-top:15px;color:var(--sub);font-size:13px;border-top:1px solid var(--line);padding-top:12px">
              <span style="cursor:pointer" data-action="like" data-id="${p.id}">❤️ ${p.likes.length} 点赞</span>
              <span style="cursor:pointer" data-nav="detail" data-id="${p.id}">💬 ${p.replies.length} 回复</span>
            </div>
          </div>
        `;
      }).join('')}
    `;

    const renderDetail = () => {
      const post = getPost(state.params.id);
      const author = getUser(post.authorId);
      return `
        <div class="panel">
          <div style="display:flex;align-items:center;gap:12px;margin-bottom:15px;cursor:pointer" data-nav="profile" data-id="${author.id}">
            <div class="avatar">${author.avatar}${author.accessory?`<div class="accessory">${author.accessory}</div>`:''}</div>
            <div><b>${author.name}</b></div>
          </div>
          <h2>${post.title}</h2>
          <div class="post-content">${post.content}</div>
        </div>
        <div class="panel">
          <h3>评论区 (${post.replies.length})</h3>
          ${post.replies.length===0?'<p style="color:var(--sub)">还没有评论，来抢沙发吧~</p>':''}
          ${post.replies.map(r => {
            const rA = getUser(r.authorId);
            return `<div style="padding:10px 0;border-bottom:1px solid var(--line)"><b style="font-size:13px">${rA.name} <span style="color:var(--sub);font-weight:normal">· ${formatTime(r.time)}</span></b><p style="margin:5px 0">${r.content}</p></div>`;
          }).join('')}
          <div style="margin-top:20px">
            <textarea id="reply-input" class="input-box" rows="3" placeholder="回复楼主..."></textarea>
            <button class="btn btn-primary" style="margin-top:10px" data-action="submit-reply" data-id="${post.id}">发送</button>
          </div>
        </div>
      `;
    };

    const renderProfile = () => {
      const user = getUser(state.params.id);
      const isMe = user.id === state.currentUser;
      const me = getUser(state.currentUser);
      const isFollowed = me.follows.includes(user.id);

      return `
        <div class="panel" style="display:flex;gap:20px;align-items:flex-start">
          <div class="avatar large">${user.avatar}${user.accessory?`<div class="accessory" style="font-size:30px">${user.accessory}</div>`:''}</div>
          <div style="flex:1">
            <div style="display:flex;justify-content:space-between">
              <h1 style="margin:0 0 10px 0">${user.name}</h1>
              ${isMe ? `<button class="btn" data-nav="edit-profile">✏️ 编辑猫设与装扮</button>` :
               `<button class="btn ${isFollowed?'':'btn-primary'}" data-action="follow" data-id="${user.id}">${isFollowed?'已关注':'关注'}</button>`}
            </div>
            <p style="color:var(--sub);margin:0 0 10px 0">${user.bio || '这只猫很懒，什么都没写'}</p>
            <div>
              <span class="chip chip-gray">${user.breed}</span><span class="chip chip-gray">${user.city}</span>
              <span class="chip chip-orange">阿贝贝：${user.abebei||'无'}</span>
            </div>
          </div>
        </div>
        <div class="panel">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:15px">
            <h3 style="margin:0">📍 去过的地方</h3>
            ${isMe ? `<button class="btn btn-sm" data-action="add-place">打卡新地点</button>` : ''}
          </div>
          ${user.places.length===0 ? '<p style="color:var(--sub);font-size:13px">还没记录地点~</p>':''}
          ${user.places.map(pl => `<div class="chip chip-green">${pl.name} - "${pl.review}"</div>`).join('')}
        </div>
      `;
    };

    const renderEditProfile = () => {
      const me = getUser(state.currentUser);
      return `
        <div class="panel">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px">
            <h2 style="margin:0">✏️ 完善猫设与装扮</h2>
            <button class="btn btn-primary" data-action="save-profile">保存修改</button>
          </div>
          <div class="field">
            <label>宠物装扮 (选择一个头饰)</label>
            <div style="display:flex;gap:10px">
              ${['','🎩','👑','🎀','🕶️','🌸'].map(acc => `
                <div class="avatar" style="cursor:pointer;border:${me.accessory===acc?'2px solid var(--pink)':'1px solid var(--line)'}" onclick="document.getElementById('acc-input').value='${acc}'; showToast('选中装扮：${acc||'无'}')">
                  ${me.avatar}<div class="accessory">${acc}</div>
                </div>
              `).join('')}
              <input type="hidden" id="acc-input" value="${me.accessory}">
            </div>
          </div>
          <div class="field"><label>名字</label><input type="text" id="ep-name" class="input-box" value="${me.name}"></div>
          <div class="field"><label>品种</label><input type="text" id="ep-breed" class="input-box" value="${me.breed}"></div>
          <div class="field"><label>城市</label><input type="text" id="ep-city" class="input-box" value="${me.city}"></div>
          <div class="field"><label>阿贝贝 (最爱的东西)</label><input type="text" id="ep-abebei" class="input-box" value="${me.abebei}"></div>
          <div class="field"><label>个性签名</label><textarea id="ep-bio" class="input-box" rows="3">${me.bio}</textarea></div>
        </div>
      `;
    };

    const renderCreate = () => `
      <div class="panel">
        <h2 style="margin:0 0 20px 0">✍️ 记录猫咪日常</h2>
        <div class="field">
          <select id="c-board" class="input-box">
            ${state.boards.map(b => `<option value="${b.id}">${b.icon} 发布到：${b.name}</option>`).join('')}
          </select>
        </div>
        <div class="field"><input type="text" id="c-title" class="input-box" placeholder="标题..."></div>
        <div class="field">
          <textarea id="c-content" class="input-box" rows="6" placeholder="正文内容..."></textarea>
        </div>
        <div style="display:flex;justify-content:space-between;align-items:center;margin-top:15px">
          <button class="btn btn-ai" data-action="ai-rewrite">✨ AI 帮我喵化润色</button>
          <button class="btn btn-primary" data-action="submit-post">🛡️ AI 风控检查并发布</button>
        </div>
      </div>
    `;

    document.addEventListener('click', (e) => {
      const nav = e.target.closest('[data-nav]');
      if (nav) {
        state.view = nav.getAttribute('data-nav');
        state.params.id = nav.getAttribute('data-id');
        saveState(); render(); window.scrollTo(0,0); return;
      }

      const action = e.target.closest('[data-action]');
      if (action) {
        const act = action.getAttribute('data-action');
        const id = action.getAttribute('data-id');

        if (act === 'login') { state.currentUser = id; state.view = 'home'; saveState(); render(); }
        else if (act === 'logout') { state.currentUser = null; state.view = 'auth'; saveState(); render(); }
        else if (act === 'like') {
          const post = getPost(id);
          if(!post.likes.includes(state.currentUser)) { post.likes.push(state.currentUser); saveState(); render(); }
        }
        else if (act === 'follow') {
          const me = getUser(state.currentUser);
          if(me.follows.includes(id)) { me.follows = me.follows.filter(x=>x!==id); showToast('已取消'); }
          else { me.follows.push(id); showToast('关注成功！成为好友啦'); }
          saveState(); render();
        }
        else if (act === 'save-profile') {
          const me = getUser(state.currentUser);
          me.name = document.getElementById('ep-name').value;
          me.breed = document.getElementById('ep-breed').value;
          me.city = document.getElementById('ep-city').value;
          me.bio = document.getElementById('ep-bio').value;
          me.abebei = document.getElementById('ep-abebei').value;
          me.accessory = document.getElementById('acc-input').value;
          state.view = 'profile'; state.params.id = me.id;
          showToast('资料与装扮更新成功！'); saveState(); render();
        }
        else if (act === 'ai-rewrite') {
          const content = document.getElementById('c-content');
          if(!content.value) content.value = "今天天气真好，";
          content.value = content.value + " 喵~ 🐾 用爪爪打字真不容易，求大家摸摸头！";
          showToast('✨ AIGC: 已为您注入猫咪口吻！');
        }
        else if (act === 'view-risk') {
          alert("【AIGC 风控拦截日志】\n- [系统] 成功拦截 1 条包含人身攻击的模型改写。\n- [系统] 自动折叠 2 条内容重复度>90%的水贴。\n\n*在真实业务中，该模块会接入大模型文本风控 API 进行实时拦截*");
        }
        else if (act === 'submit-post') {
          const title = document.getElementById('c-title').value;
          const content = document.getElementById('c-content').value;
          const boardId = document.getElementById('c-board').value;
          if(!title || !content) return showToast('标题和正文不能空');

          showToast('🛡️ AI 安全风控扫描中...', 1000);

          setTimeout(() => {
            state.posts.unshift({ id: 'p'+Date.now(), authorId: state.currentUser, boardId, title, content, tags: [], likes: [], replies: [], time: Date.now() });
            state.view = 'home';
            showToast('✅ 审核通过，发布成功！');
            saveState(); render();
          }, 1000);
        }
        else if (act === 'submit-reply') {
          const content = document.getElementById('reply-input').value;
          if(!content) return;
          getPost(id).replies.push({ id: 'r'+Date.now(), authorId: state.currentUser, content, time: Date.now() });
          showToast('回复成功！'); saveState(); render();
        }
        else if (act === 'add-place') {
          const pName = prompt('输入地点名称：');
          if(pName) {
            getUser(state.currentUser).places.unshift({name: pName, status: '去过', review: '新打卡的地方喵'});
            showToast('打卡成功！'); saveState(); render();
          }
        }
      }
    });

    render();
  </script>
</body>
</html>