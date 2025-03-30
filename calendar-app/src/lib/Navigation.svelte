<script lang="ts">
	function toggleDropdown() {
		console.log('Dropdown toggled');
	}
</script>

<div class="navigation">
	<div class="logo">WØRK</div>
	<div class="nav-options">
		<a href="/">HOME</a>
		<a href="/subs">REQUEST A SUB</a>
		<a href="/availability">AVAILABILITY</a>
	</div>
</div>

<style>
	.navigation {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 30px;
		background: black;
		color: white;
		font-size: 24px;
	}

	.logo {
		font-size: 30px;
	}

	.nav-options {
		margin-top: 3px;
		display: flex;
		gap: 30px;
	}

	a {
		text-decoration: none;
		font-weight: 400;
		color: white;
		border-bottom: 5px solid transparent;
	}

	a:hover {
		border-bottom: 5px solid var(--primary-blue);
	}
</style>
