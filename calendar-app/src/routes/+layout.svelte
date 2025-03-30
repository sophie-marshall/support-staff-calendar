<script lang="ts">
	import '../global.css';

	import Navigation from '$lib/Navigation.svelte';

	let { children } = $props();
</script>

<div class="layout">
	<nav>
		<Navigation />
	</nav>
</div>

{@render children()}
