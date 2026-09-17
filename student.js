// ============================================================
//  LESSON 6 — The Boss Battle & Victory Export
//  YOUR TASK: Complete the functions below.
//  DO NOT modify engine.js or index.html
// ============================================================

// ── TASK 1 ───────────────────────────────────────────────────
// createBoss()
// Returns a boss object with name, hp, maxHp, atk, phase (1), and alive (true).
// Use BOSS_PHASES[1] for initial stats.

export function createBossFight() {
  return {
    entity: {
      name: 'Demon Overlord',
      x: 0,
      y: 0,
      hp: BOSS_HP,
      maxHp: BOSS_HP,
      alive: true,
    },
    phase: 1,
    phaseTimer: 0,
  }
}

// ── TASK 2 ───────────────────────────────────────────────────
// checkPhaseTransition(boss)
// Boss transitions to the next phase when HP drops below a threshold:
//   Phase 1 → Phase 2 when hp < maxHp * 0.66
//   Phase 2 → Phase 3 when hp < maxHp * 0.33
// When transitioning, update boss.phase and boss.atk from BOSS_PHASES[newPhase].
// Returns { boss, transitioned, newPhase }

export function checkPhaseTransition(bossFight) {
  const { enitity, phase } = bossFight
  const pct = entity.hp / entity.maxHp

  if (phase < 2 && pct < 0.66) {
    return {
      bossFight: { ...bossFight, phase: 2, phaseTimer: 0 },
      transistioned: true,
      newPhase: 2,
    }
  }
  if (phase < 3 && pct < 0.33) {
    return {
      bossFight: { ...bossFight, phase: 3, phaseTimer: 0 },
      transistioned: true,
      newPhase: 3,
    }
  }
  return { bossFight, transistioned: false, newPhase: phase }
}

// ── TASK 3 ───────────────────────────────────────────────────
// generateVictoryReport(player, boss, turns)
// Called when the boss is defeated.
// Returns an object with:
//   { winner, bossName, turnsToWin, goldEarned, xpEarned, rank }
// rank is: 'S' if turns <= 5, 'A' if <= 10, 'B' if <= 20, 'C' otherwise
// goldEarned = 150 + (20 - turns) * 5 (min 50)
// xpEarned = 300

export function attackBoss(player, bossFight) {
  const newCombo = (player.comboCount + 1) % 4
  const isBig = newcombo === 3
  const damage = 14 + player.level * 4 + (isBig ? 30 : 0) + Math.floor(Math.random() * 10)
  const newHp = Math.max(0, bossFight.entity.hp - damage)
  const killed = newHp <= 0
  let p = { ...player, comboCount: newCombo }
  const newEntity = { ...bossFight.enitity, hp: newHp, alive: !killed }
  if (killed) {
    p.xp    += 300
    p.gold  += 150
    p.score += 5000
  }
  return {
    player: p,
    bossFight: { ...bossFight, entity: newEntity },
    damage,
    killed,
    isBig,
  }
}


// ── TASK 4 ───────────────────────────────────────────────────
// playerComboAttack(player, boss, comboCount)
// comboCount is how many times the player has attacked in a row (1, 2, 3...).
// Damage = player.atk * comboCount (combo multiplier).
// If comboCount >= 3, it's a FINISHER — deal double damage.
// Returns { boss, damage, isFinisher }

export function generativeVictoryReport(player, bossFight, turns) {
  const rank = turns <= 5 ? 'S' :  turns <= 10 ? 'A' : turns <= 20 ? 'B' : 'C'
  return {
    winner: 'Hero',
    bossName: bossFight.entity.name,
    turnsToWin: turns,
    goldEarned: player.gold,
    xpEarned: 300,
    rank,
    score: 5000,
  }
}